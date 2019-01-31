# MINT QuickStart Guide

## Overview

![MINTAnalysis](https://github.com/mintproject/MINT_USERGUIDE/blob/master/Figures/MainControlPanel.jpg?raw=true)

The MINT user interface is organized around the following concepts:
* **Explore a region of interest**.  The top green panel allows a user to: (1) upload and browse CAGs of variables automatically extracted from  documents and edit them to add more variables, (2) browse (and upload) datasets for the region, and (3) generate new data by processing remote sensing data or probabilistic predictions for prognostic scenarios.  

* **State a question**. The left yellow panel allows a user to: (4) jot down a [question](#question_def), and to indicate the region and timeframe for that question.  

* **Work on a question**. The middle blue panel (5) allows a user to carry out [tasks](#task_def) to work on a selected question by: (a) selecting [driving](#drivingvar_def) and [response](#responsevar_def) variables, (b) selecting datasets for the driving variables, (c) choosing and composing models, (d) running models, and (e) visualizing the results (7). User choices are recorded and shown in the grey panel (8) at the bottom left.

* **Work on a task**.  When a task is selected, the orange panel (6) in the right guides the user through [activities](#activity_def) to accomplish it.  Each type of task involves different activities, which are done in sequence.  Some of these activities involve selecting and running [workflows](#workflow_def) composed of models and data transformations.  MINT will always generate the workflows, and may fill some of the inputs (which will use driving variables) with the user's previous choices (eg the region or time period).  MINT executes the workflow efficiently in high-performance computing resources, but becasuse this may take some time it will run them in the background and let the user continue to explore other questions.  Once finalized, the resulting datasets can be archived for future use.  When a dataset is archived, MINT will suggest metadata and the user can provide additional metadata as they consider appropriate.



* **Task 1**: Browse the CAG to get a better understanding of the causality among various variables (1 in <a name='fig1'>Figure 1</a>).
* **Task 2**: Visualize a dataset present in the data catalog. (2 in <a name='fig1'>Figure 1</a>). In the dataset name, enter FLDAS, for instance. Click on the graph icon next to the dataset of interest.
* **Task 3:**: Formulate a problem by adding a question in the QUESTIONS panel. You can formulate any problem you want. This is a reference to keep tack of a particular problem (4 in <a name='fig1'>Figure 1</a>).
*Example*: Is flooding expected in the Pongo Basin area during the upcoming growing season (April - March) 2017?
* **Task 4:** With the question from step 3 selected, run through the various tasks (5 in <a name='fig1'>Figure 1</a>):
  * Select the [driving](#drivingvar_def) and [response variables](#responsevar_def) from the CAG.
  *Example*: Select rainfall as the driving variable and flooding as the response variable.
  * Select datasets for the analysis. MINT will offer suggestions based on the chosen driving variable.
  * Compose and select workflow (6 in <a name='fig1'>Figure 1</a>). MINT will offer a workflow based on the driving and
  * Visualize the results (7 in <a name='fig1'>Figure 1</a>)

## Glossary
<a name="activity_def">**Activity**</a>: Users go through a series of activities in order to accomplish a task.  In MINT, activities are shown in the orange panel on the bottom right.
<a name="cag_def">**Causal Analysis Graph (CAG)**</a>: A graph where nodes are modeling variables linked by causal relations.   
<a name="drivingvar_def">**Driving variable**</a>: The variable that will influence a response in the system.  
<a name="question_def">**Question**</a>: A string that states what the user is currently looking into, and may include the selection of a region and a time period. 
<a name="responsevar_def">**Response variable**</a>: The variable that will show the impact of the driving variable onto the system.
<a name="task_def">**Task**</a>: Users go through a series of tasks in order to answer a question of interest. In MINT, tasks are shown in the blue panel in the middle of the screen.
<a name="workflow_def">**Workflow**</a>: In the MINT system, a workflow is a composition of models and data transformation steps necessary to investigate the effect of the [driving variable](#drivingvar_def) onto the [response variable](#responsevar_def).
