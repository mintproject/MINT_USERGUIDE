# A Quick Guide to the MINT Model Catalog
## Overview
The MINT Model Catalog is a metadata registry that describes physical, environmental and social models (e.g., climate, hydrology, agriculture or economy models) in order to:

 * **Help finding models**, filtering them by their name, keywords, variables or region where they can be executed.
 * **Execute models**, either by providing new input files and parameters or by choosing pre-selected models setup by experts.  
 * **Understand how to use models** and interpret their results. We need to describe the variables included in the input files  of each model in order to help users selecting appropriate data for execution. Similarly, we need to describe the output variables of the results, or otherwise users will have to interpret them themselves. Other geospatial and temporal information is critical for providing the right context to understand model results.

Figure 1 shows and overview of the main categories we use to irganize the model catalog, which are further in the following sections.

![Overview of the Model Catalog capabilites](figures/overview.png "Overview of the model catalog")*Fig. 1: Overview of the Model Catalog's main categories  for finding, executing and understanding models.*

!!! tip "Quick links"
    * GUI for exploring the contents of the model catalog: [https://models.mint.isi.edu/home](https://models.mint.isi.edu/home)
    * REST API for adding/modifying/deleting model catalog contents: [https://api.models.mint.isi.edu/v1.3.0/ui/#/](https://api.models.mint.isi.edu/v1.3.0/ui/#/)
    * [Requires log in] GUI for configuring and editing models: [https://mint.isi.edu/ethiopia/models/configure](https://mint.isi.edu/ethiopia/models/configure)

## Making your model findable
--------
This is the simplest way to describe a model so other modelers understand what it does without going into much detail. Models **do not need** to be executable in order to be included in the model catalog. Making the model findable ensures that it has minimum metadata to describe its attribution, proper citation and (if they exist) pointers to the website, creator, license and maintainer. Models usually have a description, basic keywords and relevant assumptions that have to be considered before their usage.

### Model and model versions
We include two main levels of granularity for making models findable. The first involves describing the model itself, at a generic level. The second level describes the model version (or versions) available in the catalog. This is required because models under continuous development may have multiple co-existing versions with different characteristics. Figure 2 shows an example for a common groundwater model, which has two different versions that are used for different purposes and developed by different researchers.

![Model configuration versus model configuration setup](figures/version.png "Model configuration versus model configuration setup")*Fig. 2: Capturing models and model versions.*

## Making your model executable
--------
One of the reasons for including a model in the model catalog is to make it available for execution with different files and parameters values. For example, let's consider the model shown in Figure 3, which invokes a python wrapper for the TopoFlow model using two *input files* (precipitation and configuration files) and two *parameters* (hydrologic conductivity and the simulation years to run the model), which set up numerical options for the model:

<img src="figures/component.png" width="300">

*Fig. 3: TopoFlow model component with 2 input files, 2 input parameters and 2 outputs.*

We may want to execute this model in a region with a certain  configuration file and precipitation rates, or we may want allow users changing both of these files to the files they created themselves. In order to support this flexibility, 
We distinguish the following concepts for executing models: 

### Model configuration
Represents a unique way of running a model, exposing concrete inputs, outputs and parameters. Here we refer to *model inputs/outputs* 

The same version of a model may have different model configurations.

### Model configuration setup
Represents a model configuration with parameters and files that have been adjusted (manually or automatically) to ease its execution. Model configuration setups may expose no inputs (for example, if the model has been calibrated to be run in a specific region) and may hide some of the outputs of the model (e.g., if the creator if the setup considered them irrelevant for the region at hand). Parameters may also be adjusted to fixed values (e.g., only considering a few simulation years), or restricted (changing their maximum and minimum accepted values) to make sure users obtain consistent results. For example, in Figure 3 the hydrologic conductivity in the right was adjusted to a constant value by a domain expert for the region of the analysis. 

Let's illustrate this with the example below.

![Model configuration versus model configuration setup](figures/mc_ms.png "Model configuration versus model configuration setup")*Fig. 4: Main differences between model configuration and model configuration setup. While model configuration expose all the files and parameters needed to execute a model (2 files and 2 parameters on the left), the model configuration setup on the right simplify them for end users (only precipitation rates and simulation years are exposed).*

!!! tip "When should you use model configurations versus model configuration setups?"
    If you want to make a model executable but you want to fix a subset of its configuration files for a particular region or period of time so users don't have to deal with it, then it's a model configuration setup. Setups allow for hiding parameters or configuration files to end users, who may not be interested in that level of complexity.

### Model inputs, outputs and parameters

## Making your model understandable
--------

    Explain that this is not needed for the model to be executable, but helps a lot for interpreting results and finding the right data

### Variables and Units

### Grid

### Region

### Time Step