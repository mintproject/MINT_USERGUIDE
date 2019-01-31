# MINT QuickStart Guide

MINT is currently configured to work with models to explore climate-related questions in select regions of South Sudan.

![MINTAnalysis](https://github.com/mintproject/MINT_USERGUIDE/blob/master/Figures/MainControlPanel.jpg?raw=true)

The MINT user interface is organized around the following concepts:

* **Explore a region of interest**.  The top green panel allows a user to: (1) upload and browse [CAGs](#cag_def) of variables automatically extracted from  documents and edit them to add more variables, (2) browse (and upload) datasets for the region, and (3) generate new data by processing remote sensing data or probabilistic predictions for prognostic scenarios.  

* **State a question**. The left yellow panel allows a user to: (4) jot down a [question](#question_def), and to indicate the region and timeframe for that question.  

* **Work on a question**. The middle blue panel (5) allows a user to carry out [tasks](#task_def) to work on a selected question by: (a) selecting [driving](#drivingvar_def) and [response](#responsevar_def) variables, (b) selecting datasets for the driving variables, (c) choosing and composing models, (d) running models, and (e) visualizing the results (7). User choices are recorded and shown in the grey panel (8) at the bottom left.

* **Work on a task**.  When a task is selected, the orange panel (6) in the right guides the user through [activities](#activity_def) to accomplish it.  Each type of task involves different activities, which are done in sequence.  Some of these activities involve selecting and running [workflows](#workflow_def) composed of models and data transformations.  MINT will always generate the workflows, and may fill some of the inputs (which will use driving variables) with the user's previous choices (eg the region or time period).  MINT executes the workflow efficiently in high-performance computing resources, but becasuse this may take some time it will run them in the background and let the user continue to explore other questions.  Once finalized, the resulting datasets can be archived for future use.  When a dataset is archived, MINT will suggest metadata and the user can provide additional metadata as they consider appropriate.

## Glossary
<a name="activity_def">**Activity**</a>: Users go through a series of activities in order to accomplish a task.  In MINT, activities are shown in the orange panel on the bottom right.

<a name="cag_def">**Causal Analysis Graph (CAG)**</a>: A graph where nodes are modeling variables linked by causal relations. 

<a name="drivingvar_def">**Driving variable**</a>: The variable that will influence a response in the system.  

<a name="question_def">**Question**</a>: A string that states what the user is currently looking into, and may include the selection of a region and a time period. 

<a name="responsevar_def">**Response variable**</a>: The variable that will show the impact of the driving variable onto the system.

<a name="task_def">**Task**</a>: Users go through a series of tasks in order to answer a question of interest. In MINT, tasks are shown in the blue panel in the middle of the screen.

<a name="workflow_def">**Workflow**</a>: In the MINT system, a workflow is a composition of models and data transformation steps necessary to investigate the effect of the [driving variable](#drivingvar_def) onto the [response variable](#responsevar_def).
