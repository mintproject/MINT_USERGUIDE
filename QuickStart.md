# MINT QuickStart Guide

## Introduction

The MINT user interface is designed around a main task panel ([Analysis](http://mint-system.org/govern/analysis/south_sudan)) from which an analyst can:
* **Formulate their problem**. MINT assists the user in the formulation of their problem by letting them (1) visualize existing causal analysis graphs ([CAG](#cag)) or upload their own CAG into the system and (2) formulate their modeling question(s).
* **Explore existing data on the region of interest**. The "browse data" window allows to explore existing datasets within the MINT data catalog, a useful feature for problem formulation and modeling setup. New datasets can be added through the [registration interface](http://mint-system.org/results/publish).
* **Generate new datasets through pre-defined workflows**. The user can generate new datasets from pre-defined workflows, including probabilistic weather data for prognostic scenarios.
* **Compose and execute [workflows](#workflow_def) given a set of [driving](#drivingvar_def) and [response variables](#responsevar_def)**. MINT suggests appropriate models for the target variables, along with transformations to run them together as a workflow. MINT executes the workflow efficiently in high-performance computing resources, and stores any results for future use.
* **Visualize the results of the workflow**. MINT associates common visualizations to different types of data, and uses them to present results to the users.

## MINT Analysis

The [MINT Analysis] panel (http://mint-ui.org/govern/analysis/south_sudan) allows to access all the components of the MINT system. It is designed to keep track of all the steps in an analysis (<a name='fig1'>Figure 1</a>).

![MINTAnalysis](https://github.com/mintproject/MINT_USERGUIDE/blob/master/Figures/MainControlPanel.jpg?raw=true)
*[Figure 1](#fig1): Overview of the MINT Analysis panel. From here an analyst can (1) examine a CAG, (2) Browse existing datasets or upload a new one to the data catalog, (3) generate new data through pre-exiting workflows, (4) formulate a problem, (5) select various tasks in answer of the formulated problem, (6) compose and execute workflows, and (7) visualize the results. MINT keeps track of all the choices a user made in its provenance catalog. The provenance is displayed on the Analysis panel (8).*

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
<a name="cag">**Causal Analysis Graph**</a>: Graphical models used to encode causal inference and community this causality from data.   
<a name="drivingvar_def">**Driving variable**</a>: The variable that will influence a response in the system.  
<a name="responsevar_def">**Response variable**</a>: The variable that will show the impact of the driving variable onto the system  
<a name="workflow_def">**Workflow**</a>: In the MINT system, a workflow is a composition of models and data transformation steps necessary to investigate the effect of the [driving variable](#drivingvar_def) onto the [response variable](#responsevar_def).
