# Overview of Interventions Currently Supported in MINT

Interventions in MINT reflect human actions that can change the course of a system’s behavior. Currently, the models in MINT supports an analyst to explore three kinds of interventions: fertilizer subsidies, planting windows, and weed control methods.

In MINT, an intervention is linked to an adjustable parameter of a model. The table below summarizes the interventions that MINT currently supports.

| **Intervention** | **Description** | **Model** | **Adjustable Parameter(s)** |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fertilizer subsidies | Interventions concerning fertilizer subsidies can be expressed in this model as a percentage of fertilizer prices | EACS | `sesame-fertilizer-cost-adjustment`, `cassava-fertilizer-cost-adjustment`, `maize-fertilizer-cost-adjustment`, `sorghum-fertilizer-cost-adjustment`, `groundnuts-fertilizer-cost-adjustment` |
| Planting windows | Interventions that force specific target planting windows can be expressed in this model as start and end planting dates | Cycles | `start-planting-day`, `end-planting-day` |
| Weed control | Interventions concerning weed control and weed management practices can be reflected in this model by indicating the fraction of weeds that will remain after the weed treatments applied by farmers | Cycles | `weed-fraction` |

There are two specific places in the MINT user interface where interventions can be seen:

 * The MINT Model Catalog. There is documentation about interventions under the Parameters and Inputs tab. The parameters table has a column called “Relevant Interventions”, and hovering over the intervention shows its description.
 * The Modeling Task Editor. When an adjustable variable is chosen that has an associated intervention there is a description of the intervention shown.
 * The Setup step in the Use Models tab. When the adjustable parameters are edited, the documentation shows when an intervention can be considered.

For example, an intervention that could be explored is providing fertilizer subsidies to farmers. This can be explored with the EACS economic model by adjusting the parameters concerning the cost of fertilizers for each crop type. The maize fertilizer price adjustment parameter reflect the percentage change in the unit cost of nitrogen fertilizer as an input into the production of maize, where a reduction in the unit cost of nitrogen fertilizer for maize can be interpreted as a fertilizer subsidy for maize. The range of this parameter is from *-50* to *50*. So a value of this parameter of *-10* reflects a moderate subsidy. The model takes into account farmer’s behaviors when fertilizer cost is lower, and will adjust crop production accordingly.
