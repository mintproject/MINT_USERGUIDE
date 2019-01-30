# Mint User Guide

## Table of Contents
[MINT user Interface]()

## MINT User Interface

The MINT UI is designed around a main task panel ([Analysis](http://mint-ui.org/govern/analysis/south_sudan)) from which an analyst can:
* **Formulate their problem**. MINT assists the user in the formulation of their problem by letting them (1) visualize existing causal analysis graphs ([CAG](#cag)) or upload their own CAG into the system and (2) formulate their modeling question.
* **Explore existing data on the region of interest**. The "browse data" window allows to explore existing datasets within the MINT data catalog, a useful feature for problem formulation and modeling setup. New datasets can be added through the [register dataset page](http://mint-ui.org/results/publish).
* **Generate new datasets through pre-defined workflows**. The system can accept new datasets that the user need to describe or generate new datasets from pre-defined workflows, such as generating probabilistic weather data for prognostic scenarios.
* **Compose and execute [workflows](#workflow_def) given a set of [driving](#drivingvar_def) and [response variables](#responsevar_def)**.MINT suggests appropriate models for the target variables, along with transformations to run them together as a workflow. MINT executes the workflow efficiently in high-performance computing resources, and stores any results for future use.
* **Visualize the results of the workflow** MINT associates common visualizations to different types of data, and uses them to present results to the users.

<Insert picture of the MINT interface when ready>
*[Figure 1](#fig1): An overview of the main features of the MINT user interface.*

## South Sudan Scenario
### Background on South Sudan

The Republic of South Sudan gained  its independence from the Republic of the Sudan in 2011. Soon after its inception, political instability followed due to a power struggle. The country has been immersed in civil conflict since December 2013, resulting in severely damaged agriculture, disrupted food production and distribution, loss of life, health, assets and income. South Sudan has some of the worst health indicators in the world<sup>[1](http://www.sudantribune.com/spip.php?article1616), [2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1179754)</sup> and is prone to famines. Famine led to deaths in Northern Bahr El Ghazal and Warrap states in the mid-2011.

On February 2017, South Sudan and the United Nations declared a famine in parts of former Unity State, with the warning that it could spread rapidly without further action. Over 100,000 people were in imminent danger of death by starvation. The reason of the famine is unclear as of April 2017 but it is thought to be a consequence of drought and road blockage.

![Example CAG](https://github.com/KnowledgeCaptureAndDiscovery/MINT_USERGUIDE/blob/master/Figures/ExampleCAG.png?raw=true)  
*Figure 2: Example of a Causal Analysis Graph (CAG) depicting the relationship among the various factors leading to poverty in South Sudan*

Based on the example CAG above, an analyst may wish to investigate the role of precipitation in food security during the 2017 lean season.

South Sudan has a mostly tropical climate with a rainy season with large amounts of rainfall from April to October followed by a dry season. It is also impacted by severe weather events, resulting in flooding. During flooding events, farmers are unable to plant their crop, leading to planting delays and potentially crop failure.

This tutorial follows the steps an analyst may undertake within the MINT framework to understand how precipitation could lead to a famine in South Sudan in summer 2017.

### Analyst's tasks

#### Formulating the problem

The first task in any analysis is problem formulation. It is often done in the form of a question or a series of questions that reflect upon the analyst's understanding of the situation. This often involves background reading and/or examining CAGs obtained from machine readers, for instance.

`On the analysis page, click on Browse CAG` (<a name='fig1'>Figure1</a>).

The CAG prepared by the University of Pittsburg's team loads into the main window (<a name='fig3'>Figure 3</a>).

![BROWSECAG](https://github.com/KnowledgeCaptureAndDiscovery/MINT_USERGUIDE/blob/master/Figures/BrowseCag.png?raw=true)  
*[Figure 3](#fig3): CAG prepared by the University of Pittsburg's team*

The CAG infers a causal relationship between rainfall, flooding, planting, and crop production (<a name='fig4'>Figure 4</a>). As a starting point, the analysts decides to better understand the connection between these 4 variables since precipitation and crop-production are nodes with lots of connections in the CAG. The CAG informs the user that rainfall is the [driving variable](#drivingvar_def) while crop production is the main [response variable](#responsevar_def).  

![CAGZoom](https://github.com/KnowledgeCaptureAndDiscovery/MINT_USERGUIDE/blob/master/Figures/CAGZoom.png?raw=true)  
*[Figure 4](#fig4): Close-up view of a subsection of the CAG relating precipitation to crop-production selected for further analysis.*

The problem can be further broken down as follows:
* Is flooding expected in the Pongo Basin area during the upcoming growing season (April-August) 2017?
* What is the expected crop yield for maize and sorghum?
* When is the best planting window to ensure optimum yields?
* Would subsidies help farmers adapt to changing conditions during the growing season?

The reminder of this tutorial is formulated around answering these four main questions. Please note that the question template is open-ended but allows to keep track of the analyses that have been performed.

`Enter the first question in the QUESTIONS interface by clicking on '+ADD NEW QUESTION'. Enter the question in the new interface and select region. Click OK.` (<a name='fig5'>Figure 5</a>)

![QuestionUI](https://github.com/KnowledgeCaptureAndDiscovery/MINT_USERGUIDE/blob/master/Figures/QuestionsInterface.jpg?raw=true)  
*[Figure 5](#fig5): Questions panel in the MINT Analysis interface*  

Repeat the procedure for the next three questions. You will be allowed to formulate more questions later depending on the results of the analysis.

#### Identifying [driving](#drivingvar_def) and [response variables](#responsevar_def)

For each of the questions, the user is then asked to select the [driving variable](#drivingvar_def) and the [response variable](#responsevar_def).

`Click on the first question in the QUESTION panel to select it.`

Several tasks will become available in TASKS panel (<a name='fig6'>Figure 6</a>).

![TasksPanel](https://github.com/KnowledgeCaptureAndDiscovery/MINT_USERGUIDE/blob/master/Figures/TaskPanel.png?raw=true)  
*[Figure 6](#fig6): TASKS available from the MINT Analysis interface.*

`Click on 'Select Variables'.` to list the possible activities related to this task (<a name='fig7'>Figure 7</a>).

![ActivtiesPanel](https://github.com/KnowledgeCaptureAndDiscovery/MINT_USERGUIDE/blob/master/Figures/ActivitiesPanel.png?raw=true)  
*[Figure 7](#fig7): ACTIVITIES available from the MINT Analysis interface under the 'Select Variables' task.*

The UI is asking to identify the [driving](#drivingvar_def) and [response variable](#responsevar_def) for the question. In this case, the [driving variable](#drivingvar_def) is *rainfall* and the [response variable](#responsevar_def) is *flooding*.

`Click on 'Select Driving Variable' and click on the variable name in the CAG. Click DONE at the top of the window.` (<a name='fig8'>Figure 8</a>)

![VarSelection](https://github.com/KnowledgeCaptureAndDiscovery/MINT_USERGUIDE/blob/master/Figures/VarSelection.png?raw=true)  
*[Figure 8](#fig8): Selecting the driving variable*

`Repeat the process for the response variable.`

Once you are done, the 'Select Driving Variables' and 'Select Response Variables' activities should turn green with a check mark next to them. In addition, the 'YOUR SELECTIONS' panel keeps tracks of the choices made. (<a name='fig9'>Figure 9</a>)

![History](https://github.com/KnowledgeCaptureAndDiscovery/MINT_USERGUIDE/blob/master/Figures/History.png?raw=true)  
*[Figure 9](#fig9) YOUR SELECTIONS panel in the MINT Analysis interface keep track of the user's choices at every step of the analysis.*

#### Selecting, exploring, and comparing datasets

`Click on Select Datasets in the TASKS panel.`

From the activities panel, you will be able to 'Find and Select Datasets', 'Run Data Exploration Workflows', or 'Run Data Exploration Workflows'.

`Click on Find and Select Datasets.`

The search engine returns the datasets associated with the [driving variable](#drivingvar_def) of interest (i.e., rainfall) for the selected sub-region in the QUESTIONS panel.

`Select all datasets of interest and click DONE.`

<VIZ?>

To add new datasets, go to [BLANK](http://mint-ui.org/results/publish) to register the data (see the tutorial [here](#registerdata)).

To understand how precipitation could affect food supply in the future, it is often useful to look at the prediction in its historical context. One simple task is to visualize the datasets (***Fig 10?***). In addition, users can use pre-defined workflows to transform the data for visualization. For instance, the ClimComp workflow allows to look at seasonal averages rather than the entire year, which may be more useful when considering the growing season.

`In the ACTIVITIES panel, click on 'Run Data Exploration Workflows'. Select CLIMCOMP. Click on RUN WORKFLOW.`

<finish with preloading.>



#### Generating new data

Sometimes an analyst may need to generate new data, either to get a better understanding of the problem or to run probabilistic scenarios from historical data.

For instance, probabilistic weather forecast from a weather generator is a good alternative to numerical forecast, which may not be accurate too far into the future.

<What can the user select... Q1c>

Similarly, using one the pre-defined workflow in MINT, an analyst can extract historical water depth for a river from satellite imagery by using machine learning techniques for remote sensing data.

<Generating new data using remote sensing workflows... not a Q>

### Other Tasks

#### <a name='registerdata'> Registering new datasets </a>

#### <a name='otherregions'> Selecting another region </a>

## Glossary
<a name="cag">**Causal Analysis Graph**</a>: Graphical models used to encode causal inference and community this causality from data.   
<a name="drivingvar_def">**Driving variable**</a>: The variable that will influence a response in the system.  
<a name="responsevar_def">**Response variable**</a>: The variable that will show the impact of the driving variable onto the system  
<a name="workflow_def">**Workflow**</a>: In the MINT system, a workflow is a composition of models and data transformation steps necessary to investigate the effect of the [driving variable](#drivingvar_def) onto the [response variable](#responsevar_def).
