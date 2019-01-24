# Mint User Guide

## Table of Contents
[MINT user Interface]()

## MINT User Interface

The MINT UI is designed around a main task panel ([GOVERN](http://mint-ui.org/govern/home)) from which an analyst can:
* Formulate their problem
* Explore existing data on the region of interest and
* Generate new datasets through pre-defined workflows
* Compose and execute [workflows](#workflow_def) given a set of [driving](#drivingvar_def) and [response variables](#responsevar_def).
* Visualize the results of the workflow.

<Insert picture of the MINT interface when ready>

### Problem Statement

### Explore existing datasets

### Generate new datasets through pre-defined workflows

### Compose and execute workflows

### Visualize results

## South Sudan Scenario
### Background on South Sudan

The Republic of South Sudan gained  its independence from the Republic of the Sudan in 2011. Soon after its inception, political instability followed due to a power struggle. The country has been immersed in civil conflict since December 2013, resulting in severely damaged agriculture, disrupted food production and distribution, loss of life, health, assets and income. South Sudan has some of the worst health indicators in the world<sup>[1](http://www.sudantribune.com/spip.php?article1616), [2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1179754)</sup> and is prone to famines. Famine led to deaths in Northern Bahr El Ghazal and Warrap states in the mid-2011.

On February 2017, South Sudan and the United Nations declared a famine in parts of former Unity State, with the warning that it could spread rapidly without further action. Over 100,000 people were in imminent danger of death by starvation. The reason of the famine is unclear as of April 2017 but it is thought to be a consequence of drought and road blockage.

![Example CAG](https://github.com/KnowledgeCaptureAndDiscovery/MINT_USERGUIDE/blob/master/Figures/ExampleCAG.png?raw=true)
*Example of a Causal Analysis Graph (CAG)depicting the relationship among the various factors leading to poverty in South Sudan*

Based on the causal analysis graph (CAG) above, an analyst may investigate the role of precipitation in the food security during the 2017 lean season. South Sudan has a mostly tropical climate with a rainy season with large amounts of rainfall from April to October followed by a dry season. It is also impacted by severe weather events, resulting in flooding. During flooding events, farmers are unable to plant their crop, leading to planting delays and potentially crop failure.

This tutorial follows the steps an analyst may undertake within the MINT framework to understand how precipitation could lead to a famine in South Sudan in summer 2017.

### Analyst's tasks

#### Formulate the problem

The first task in any analysis is problem formulation. It is often done in the form of a question or a series of questions that reflect upon the analyst's understanding of the situation. This often involves background reading and/or examining CAGs obtained from machine readers.

<Look at the CAG direction>

In the case of our South Sudan scenario, an analyst may break down the problem as follows:
* Is flooding expected in the Pongo Basin area during the upcoming growing season (April-August) 2017?
* What is the expected crop yield for maize and sorghum?
* When is the best planting window to ensure optimum yields?
* How can farmers adapt to changes in precipitation during the 2017 growing season?
* Would subsidies help farmers adapt to changing conditions during the growing season?

MINT allows the analyst to keep track of their questions and the analyses they have conducted to answer them.

<description on how to actually do that>

For each of the questions, the user is then asked to select the [driving variable](#drivingvar_def) and the [response variable](#responsevar_def).

#### Examining existing data

To understand how precipitation could affect food supply in the future, it is often useful to look at the prediction in its historical context.

<insert information on browsing historical data and accompanying visualization Q1a - Q1b>.

#### Generating new data

Sometimes an analyst may need to create probabilistic weather forecast from historical data rather than rely on numerical forecast, which may not be accurate too far into the future.

To do so, the analyst can generate new data using a weather generator from the pre-defined workflows.

<What can the user select... Q1c>
<Generating new data using remote sensing workfows... not a Q>

####

## Glossary
<a name="drivingvar_def">Driving variable</a>: The variable that will influence a response in the system.  
<a name="responsevar_def">Response variable</a>: The variable that will show the impact of the driving variable onto the system  
<a name="workflow_def">Workflow</a>: In the MINT system, a workflow is a composition of models and data transformation steps necessary to investigate the effect of the [driving variable](#drivingvar_def) onto the [response variable](#responsevar_def).
