# Feature_cost_estimation

Short Description:
The data set is used to make a ML model to estimate the cost of the features for given total cost of the operation in terms o fcpu_flytes served.
The final cost per-request or the dependent variable for the request might be influenced by a combination of features rather than by each one of them independently. For example of the features that are activated based on the request metadata will have a fixed cost, but some features like gzip are not just dependent on the enablement of gzip as a feature but also on the file size, which is a different independent feature by itself. Combination of different sets of independent features can influence the cost of a request, but as long as they are independent across the application space, we should be able to realize the cost coefficients of these features through the simple linear regression schemes.
Once we are able to compute the cost or coefficients of individual features, it would be easy to verify how the model is performing by looking at some examples of features that have a know fixed cost like TLS key-singings. Independent openssl speed tests can help us cross verify if the cost estimated by the LR model is close to the cost estimated by openssl's speed test.

## Go through the Final Presentation for the brief dataset EDA and Model Results.

Tests:
We can also carry out partial F Test to check the relevance of the coefficients obtained in the model.

## Added a script bigfile_to_csv.py that resolves the issue of converting large log file to csv file on the tools which otherwise required big ram memory to expand and process and which earlier was not possible on local laptops.

### --> Instructions to use: Must copy the bigfile_to_csv.py file to folder of gal_to_csv tool for it to work and the run the python script in the terminal using python bigfile_to_csv.py
 

The tool automatically splits the file in series and processes it and then gives the final combined file as csv even on small ram machine with any large filesize.
