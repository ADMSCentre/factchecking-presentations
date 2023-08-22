# Designing and Evaluating Presentation Strategies for Fact-Checked Content

Data and code used in the CIKM’23 paper [Designing and Evaluating Presentation Strategies for Fact-Checked Content](https://www.danulahettiachchi.com/papers/cikm23.pdf).

The current study setup includes eight tasks where users are asked to read a fact-checking report and answer a set of questions. In each task, the
main task page included a link that opens the fact-checking report in a new browser tab. All user engagements (e.g., scrolls, clicks)
within the report page are recorded and tracked.

In addition, the experiment includes,

- The five-item Conspiracy Mentality Questionnaire (CMQ)
- The six-item Credibility of Science Scale (CoSS)
- Demographics questions


### Data

**Fact-checking Articles**: The current experiment includes 8 fact-checking articles, four from PolitiFact and four from RMIT ABC Fact Check. Article data and the corresponding question can be configured in ``presentation/screen/resources/articles.py`` and article metadata such as images are included in ``presentation/screen/static/screen/img``

**Questions**: Questions included in the Conspiracy Mentality Questionnaire and Credibility of Science Scale are given in ``presentation/screen/resources/questions.py`` and demographics questions can be modified at ``presentation/screen/templates/screen/demographics.html``

**Participant Information Sheet**: Add details of your institute's Ethics/IRB approval to ``presentation/screen/static/screen/files/PIS.pdf``

### Deployment

The project is configured as a standard Django project. Please read [Django documentaion](https://docs.djangoproject.com/) for more details on development and deployment. Project can be run locally, or it can be easily deployed on a platform like Heroku.

Deployment Steps

- Default settings will work for local deployment. Configure environment variables in ``presentation/presentation/.env`` and Django settings in ``presentation/presentation/settings.py`` for web deployment.
- Install project dependencies ``pip install -r presentation/requirements.txt``. A python virtual environment is recommended.
- Configure the database ``python presentation/manage.py migrate``
- Start the server ``python presentation/manage.py runserver``
- Navigate to ``http://<host>:8000/screen/start`` start the task.

Things to Note
- You may need to install [PostgreSQL](https://www.postgresql.org/download/) before installing ``psycopg2``, which is only required for web deployment.

### Data Collection

Study data will be mainly stored in two tables. `StudyRecord` table will include a row for each study participant and will include questionnaire data, demographics and details like study start time. `ReportRecord` table will include entries per user per article. It will record responses to questions related to the article and other interaction data (e.g., scroll events, clicks).


# Citation

Danula Hettiachchi, Kaixin Ji, Jenny Kennedy, Anthony McCosker, Flora
Dylis Salim, Mark Sanderson, Falk Scholer, and Damiano Spina. 2023. [Designing
and Evaluating Presentation Strategies for Fact-Checked Content](https://www.danulahettiachchi.com/papers/cikm23.pdf).
In Proceedings of the 32nd ACM International Conference on Information
and Knowledge Management (CIKM ’23), October 21–25, 2023, Birmingham,
United Kingdom. ACM, New York, NY, USA, 11 pages. https://doi.org/10.1145/3583780.3614841

## BibTeX

```bibtex
@inproceedings{hettiachchi2023designing,
 author = {Hettiachchi, Danula  and Ji, Kaixin and  Kennedy, Jenny  and
McCosker, Anthony  and Salim, Flora
Dylis  and Sanderson, Mark  and Scholer, Falk  and Spina, Damiano},
 title = {{Designing and Evaluating Presentation Strategies for Fact-Checked Content}},
 booktitle = {Proceedings of the 32nd ACM International Conference on Information
and Knowledge Management},
 series = {CIKM '23},
 abstract = {With the rapid growth of online misinformation, it is crucial to have
reliable fact-checking methods. Recent research on finding checkworthy
claims and automated fact-checking have made significant
advancements. However, limited guidance exists regarding the presentation
of fact-checked content to effectively convey verified
information to users.We address this research gap by exploring the
critical design elements in fact-checking reports and investigating
whether credibility and presentation-based design improvements
can enhance users' ability to interpret the report accurately. We
co-developed potential content presentation strategies through a
workshop involving fact-checking professionals, communication
experts, and researchers. The workshop examined the significance
and utility of elements such as veracity indicators and explored the
feasibility of incorporating interactive components for enhanced
information disclosure. Building on the workshop outcomes, we
conducted an online experiment involving 76 crowd workers to
assess the efficacy of different design strategies. The results indicate
that proposed strategies significantly improve users’ ability to accurately
interpret the verdict of fact-checking articles. Our findings
underscore the critical role of effective presentation of fact reports
in addressing the spread of misinformation. By adopting appropriate
design enhancements, the effectiveness of fact-checking reports
can be maximized, enabling users to make informed judgments.},
 year = {2023},
 doi = {10.1145/3583780.3614841},
 address = {New York, NY, USA},
 location = {Birmingham, United Kingdom},
 publisher = {Association for Computing Machinery}
}
```



# Acknowledgments

This research is partially supported by the Australian Research
Council (CE200100005, DE200100064, DE200100540). This work is part of the ARC Centre of Excellence for Automated Decision-Making and Society's project [Quantifying and Measuring Bias and Engagement](https://www.admscentre.org.au/quantifying-and-measuring-bias-and-engagement/). We thank Devi
Mallal from RMIT FactLab and the participants of the workshop
for their valuable contributions. The authors would like to acknowledge Country. This research has been carried out on the unceded lands of the Woi Wurrung and Boon Wurrung language groups of the eastern Kulin nation. We pay our respects to their Ancestors and Elders, past, present, and emerging. We respectfully acknowledge their connection to land, waters, and sky.
