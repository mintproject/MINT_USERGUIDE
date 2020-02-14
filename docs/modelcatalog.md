# A Quick Guide to the MINT Model Catalog
## Overview
The MINT Model Catalog is a metadata registry that describes physical, environmental and social models (e.g., climate, hydrology, agriculture or economy models) in order to:

 * **Help finding models**, filtering them by their name, keywords, variables or region where they can be executed.
 * **Execute models**, either by providing new input files and parameters or by choosing pre-selected models setup by experts.  
 * **Understand how to use models** and interpret their results. In order to prepare input data for model execution and ensure that users can use model results, the the most relevant variables included in the input and output files should be described. Similarly, other geospatial and temporal information is critical for providing the right context to understand model results.

Figure 1 shows and overview of the main categories we use to irganize the model catalog, which are further described in the following sections.

![Overview of the Model Catalog capabilites](figures/overview.png "Overview of the model catalog")*Fig. 1: Overview of the Model Catalog's main categories  for finding, executing and understanding models.*

!!! tip "Quick links"
    * GUI for exploring the contents of the model catalog: [https://models.mint.isi.edu/home](https://models.mint.isi.edu/home)
    * REST API for adding/modifying/deleting model catalog contents: [https://api.models.mint.isi.edu/v1.3.0/ui/#/](https://api.models.mint.isi.edu/v1.3.0/ui/#/)
    * [Requires log in] GUI for configuring and editing models: [https://mint.isi.edu/ethiopia/models/configure](https://mint.isi.edu/ethiopia/models/configure)
    * Model catalog API client and examples: [https://model-catalog-python-api-client.readthedocs.io/en/latest/](https://model-catalog-python-api-client.readthedocs.io/en/latest/)
    * Model catalog API documentation: [https://model-catalog-python-api-client.readthedocs.io/en/latest/endpoints/](https://model-catalog-python-api-client.readthedocs.io/en/latest/endpoints/)

## Making your model findable
--------
Simplest way to describe a model so other modelers understand what it does without going into much detail. Models **do not need** to be executable in order to be included in the model catalog. Making a model findable ensures that it has minimum metadata to describe its attribution, proper citation and (if they exist) pointers to the website, creator, license and maintainer. Models usually have a description, basic keywords and relevant assumptions that help others finding them easily.

### Model and model versions
We include two main levels of granularity for making models findable. The first involves describing the model itself, at a generic level. The second level describes the model version (or versions) available in the catalog. This is required because models under continuous development may have multiple co-existing versions with different characteristics. Figure 2 shows an example for a common groundwater model, which has two different versions that are used for different purposes and developed by different researchers.

![Model configuration versus model configuration setup](figures/version.png "Model configuration versus model configuration setup")*Fig. 2: Capturing models and model versions.*

## Making your model executable
--------
One of the reasons for including a model in the model catalog is to make it available for execution with different files and parameters values. For example, let's consider the model shown in Figure 3, which invokes a python wrapper for the TopoFlow hydrology model using two *input files* (precipitation and configuration files) and two *parameters* (hydrologic conductivity and the simulation years to run the model), which describe numerical options for the model:

![Model configuration versus model configuration setup](figures/component.png "Model configuration versus model configuration setup")

*Fig. 3: TopoFlow model component with 2 input files, 2 input parameters and 2 outputs.*

We may want to execute this model in a region with a certain  configuration file and precipitation rates, or we may want allow users changing both of these files to the files they created themselves. In order to support this flexibility, 
We distinguish the following concepts for executing models: 

### Model configuration
Represents a unique way of running a model, exposing concrete inputs, outputs and parameters. Here we refer to *model inputs/outputs* as the data types that are used for executing the model rather than pointing to specific files. For instance, in Figure 3 the precipitation rates is a CSV file with the information about the rain amount in an area. We use the term *parameters* to refer to those values a user may be interested changing in a model (e.g., the hydrological conductivity or the simulation years in Figure 3).

!!! hint "" 
    The same version of a model may have different model configurations, which expose different functionalities. For example TopoFlow may have another model configuration without considering infiltration, which returns different results from the one in Figure 3.

### Model configuration setup
Model configurations may have multiple parameters aimed at expert users that are too complicated for decision makers. A *model configuration setup* represents a layer of abstraction over a model configuration, simplifying it and making it easier to execute in a correct and meaningful manner. For example, let's use the example shown in Figure 3 to create a model configuration setup for a particular region: 

![Model configuration versus model configuration setup](figures/mc_ms.png "Model configuration versus model configuration setup")*Fig. 4: Main differences between model configuration and model configuration setup. While model configuration expose all the files and parameters needed to execute a model (2 files and 2 parameters on the left), the model configuration setup on the right simplify them for end users (only precipitation rates and simulation years are exposed).*

As shown in Figure 4 (right), in this model configuration setup the input file with infiltration has been adjusted to a fixed URL by an expert modeler; and the hydrologic conductivity has been set to a fixed value that has been considered reasonable for the region being studied. As a result, users would only have to select the precipitation files and simulation years whenever selecting this setup to execute. 

!!! hint ""
    Setups may have all input files initialized by expert users, allowing variation only in the parameters that may be interesting in a region. This way users can execute model ensembles of interest without worrying about complex input file selection and preparation


!!! tip "When should you use model configurations versus model configuration setups?"
    If you want to make a model executable but you want to fix a subset of its configuration files for a particular region or period of time so users don't have to deal with it, then you are preparing a model configuration setup. Setups allow for hiding parameters or configuration files to end users, who may not be interested in that level of complexity.


## Making your model understandable
--------
The final level of detail when describing models is making them easy to understand and use by others. That requires providing metadata to cover at least the following categories:

### Model inputs, outputs and parameters
Although we need to know which are the model inputs, outputs and parameters we are exposing on each configuration or setup to make models executable, these may not be described sufficiently for other researchers to understand them. For each input and output, it is recommended to provide a small description of their role when executing a model. For the model parameters, it is necessary to describe their default values and minimum and maximum values so they can be correctly set up by users.

### Variables and Units
Each input and output dataset contains variables (e.g., precipitation, temperature, soil moisture, etc.) that are used by the executable model to create simulations. In a model configuration it is desirable to describe as much as these input and output variables as possible, so as to help others understand how to prepare the data. Units are also important to understand the quantities being used and predicted by a model

!!! hint ""
    While it is not required to describe all input/output variables in a model, it is recommended to describe at least all those that are critical for selecting data (e.g., precipitation variable in the Precipitation rates file of Figure 3) and plotting results. 


### Grid
Models with a geospatial grid (e.g., hydrology) should describe the characteristics of the grid (point based, 2-D, triangular, etc.) so as help determine whether regridding is necessary. In addition, providing the coordinate projection used in the input/output data is required to know how to project it in a map.

### Region
Model configurations and setups are usually calibrated and configured by experts (manually or automatically) to be run in a region. Hence, describing the region in which the model has been prepared to run is required to understand the context of the obtained results. For example, the hydrology model shown in Figure 3 is may configured differently in regions rich on clay, with little or none infiltration.

### Time Step
Different models output data at different time steps, usually depending on the data used as input. 

## Usage Examples and Tutorial
We have prepared a set of materials to help illustrating how the model catalog API and client work.

1. Step by step example on how to search models (e.g., by keyword) with the model catalog API: [https://model-catalog-python-api-client.readthedocs.io/en/latest/models/](https://model-catalog-python-api-client.readthedocs.io/en/latest/models/)
2. Step by step example on how to retrieve the available versions of a model: [https://model-catalog-python-api-client.readthedocs.io/en/latest/modelversion/](https://model-catalog-python-api-client.readthedocs.io/en/latest/modelversion/)
3. Step by step example on how to find executable model configurations of a model: [https://model-catalog-python-api-client.readthedocs.io/en/latest/modelconfigurations/](https://model-catalog-python-api-client.readthedocs.io/en/latest/modelconfigurations/)
4. Examples on how to execute models in the model catalog with a command line client: [https://model-catalog-python-api-client.readthedocs.io/en/latest/example/](https://model-catalog-python-api-client.readthedocs.io/en/latest/example/)
