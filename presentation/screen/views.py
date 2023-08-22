import hashlib
import random, json
import uuid

from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import QuestionnaireForm, TaskResponseForm, DemographicsForm
from .resources.articles import article_list
from .resources.questions import questions
from .models import Participant, StudyRecord, ReportRecord
from .resources.constants import EXPERIMENT_VERSION


def index(request):
    return redirect('screen:start')


def report(request, article_id=1, condition_id=1):
    article = article_list[article_id - 1]

    if condition_id == 1:
        credibility = 1
        presentation = 1
    elif condition_id == 2:
        credibility = 1
        presentation = 0
    elif condition_id == 3:
        credibility = 0
        presentation = 1
    elif condition_id == 4:
        credibility = 0
        presentation = 0

    context_variables = {
        'variable': {
            'veracity_indicator': 0,
            'structure': 0,
            'summary': 0,
            'credentials': 0,
            'author': 0,
            'sources': 0
        },
        'current_task': request.session.get('current_task', 0)
    }

    if credibility == 1:
        context_variables['variable']['credentials'] = 1
        context_variables['variable']['author'] = 1
        context_variables['variable']['sources'] = 1

    if presentation == 1:
        context_variables['variable']['veracity_indicator'] = 1
        context_variables['variable']['structure'] = 1
        context_variables['variable']['summary'] = 1

    context_variables.update(article)
    return render(request, 'screen/report.html', context_variables)


def task(request):
    current_task = request.session.get('current_task', 0)
    current_article_id = request.session.get('current_article', 1)
    if request.method == 'POST':
        # returning a previous task
        if ReportRecord.objects.filter(record_id=request.session.get('current_task_id')).exists():
            # save data
            form = TaskResponseForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                form_data = form.cleaned_data
                report_record = ReportRecord.objects.get(record_id=request.session.get('current_task_id'))
                report_record.input_veracity = form_data['veracity']
                report_record.input_q1 = form_data['q1']
                report_record.input_q2 = form_data['q2']
                report_record.input_r1 = form_data['q3_1']
                report_record.input_r2 = form_data['q3_2']
                report_record.input_r3 = form_data['q3_3']
                report_record.save()

                # increment task
                current_task = current_task + 1
                request.session['current_task'] = current_task
                request.session['current_task_id'] = str(uuid.UUID(int = 0))

            else:
                error_message = 'Sorry, something went wrong when submitting your task response.'
                return render(request, 'screen/error.html', {'error_message': error_message})

        else:
            # record not initiated
            return redirect('screen:start')

    if current_task == 9:
        # completed all the tasks
        return redirect('screen:demographics')

    elif current_task == 0:
        # has not started the task
        return redirect('screen:start')

    # tasks in progress
    condition_id = request.session.get('condition_order')[current_task - 1]
    article_id = request.session.get('article_order')[current_task - 1]

    article = article_list[article_id - 1]

    if not ReportRecord.objects.filter(record_id=request.session.get('current_task_id')).exists():
        # create new task record
        study_record = StudyRecord.objects.get(record_id=request.session.get('study_record_id'))
        new_report_record = ReportRecord(study_record=study_record,
                                         condition_id=condition_id, article_id=article_id)
        new_report_record.save()
        request.session['current_task_id'] = str(new_report_record.record_id)
        print(str(new_report_record.record_id))

    context_variables = {
        'article': article_id,
        'condition': condition_id,
        'current_task': current_task,
        'questions': article['questions']
    }

    return render(request, 'screen/task.html', context_variables)


def start(request):
    if request.method == 'POST':
        # new user starting the study
        # save worker ID
        worker_id = request.POST.get('worker_id', None)
        print(worker_id)

        if Participant.objects.filter(worker_id=worker_id).exists():
            # existing user, throw error
            print('repeat')
        else:
            participant = Participant(worker_id=worker_id)
            participant.save()

            # determine condition
            o1 = [1, 2, 3, 4]
            o2 = [1, 2, 3, 4]
            random.shuffle(o1)
            random.shuffle(o2)
            condition_order = o1 + o2

            a1 = [1, 2, 3, 4]
            a2 = [5, 6, 7, 8]
            random.shuffle(a1)
            random.shuffle(a2)
            article_order = a1 + a2
            if random.choice([1, 2]) == 1:
                article_order = a2 + a1

            # create new study record
            study_record = StudyRecord(participant=participant, article_order=article_order,
                                       condition_order=condition_order, experiment_version=EXPERIMENT_VERSION)
            study_record.save()

            request.session['condition_order'] = condition_order
            request.session['article_order'] = article_order
            request.session['current_task'] = 1
            request.session['study_record_id'] = str(study_record.record_id)
            request.session['current_task_id'] = str(uuid.UUID(int = 0))

            return redirect('screen:questionnaire')

    if request.session.get('current_task', 0) > 0:
        # redirect to task page
        return redirect('screen:task')

    context_variables = {}
    return render(request, 'screen/start.html', context_variables)


def complete(request):
    return HttpResponse('Completed')


def questionnaire(request):
    current_task_id = request.session.get('current_task', 0)

    if current_task_id == 0:
        return redirect('screen:start')

    if request.method == 'POST':
        # compeleted questionnaire
        request.session['questionnaire'] = 1
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            study_record = StudyRecord.objects.get(record_id=request.session.get('study_record_id'))
            study_record.questionnaire_data = json.dumps(form.cleaned_data)
            study_record.save()
            return redirect('screen:task')
        else:
            error_message = 'Sorry, something went wrong when submitting your questionnaire response.'
            return render(request, 'screen/error.html', {'error_message': error_message})


    else:
        random.shuffle(questions['q1'])
        random.shuffle(questions['q2'])
        context_variables = {
            'q1': questions['q1'],
            'q2': questions['q2']
        }
        return render(request, 'screen/questionnaire.html', context_variables)


def demographics(request):
    current_task_id = request.session.get('current_task', 0)

    if current_task_id == 0:
        return redirect('screen:start')

    if request.method == 'POST':
        # compeleted questionnaire
        request.session['demographics'] = 1
        form = DemographicsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            study_record = StudyRecord.objects.get(record_id=request.session.get('study_record_id'))
            study_record.demographic_data = json.dumps(form.cleaned_data)
            study_record.save()
            return redirect('screen:complete')

    else:
        context_variables = {}
        return render(request, 'screen/demographics.html', context_variables)


def complete(request):
    study_record = StudyRecord.objects.get(record_id=request.session.get('study_record_id'))
    unique_code = hashlib.sha256(request.session.get('study_record_id').encode()).hexdigest()[0:24]
    study_record.unique_code = unique_code
    study_record.save()
    context = {'code': unique_code }
    return render(request, 'screen/complete.html', context)


def log(request):
    if request.method == 'POST':
        current_task = request.session.get('current_task',0)
        current_task_log = request.POST.get('current_task',-1)
        # print(int(current_task),int(current_task_log))
        if int(current_task) == int(current_task_log):
            # print(request.POST.get('log_data',''))
            ReportRecord.objects.filter(record_id=request.session.get('current_task_id')).update(user_logs = request.POST.get('log_data',''))
            return HttpResponse('OK')
        else:
            return HttpResponse('OK')