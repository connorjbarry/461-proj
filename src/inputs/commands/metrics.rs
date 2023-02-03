pub struct Metrics {
    ramp_up:f64,
    correctness:f64,
    bus_factor:f64,
    responsiveness:f64,
    license:f64,
    total:f64,
}

impl Metrics {
    pub fn new() -> Self {
        Metrics {
            ramp_up: 0.0,
            correctness: 0.0,
            bus_factor: 0.0,
            responsiveness: 0.0,
            license: 0.0,
            total: 0.0,
        }
    }

    /* 
        Function: get_ramp_up
        Arguments: module_name - the name of the module the metric is graded for
        Return: f64 - between 0 and 1

        Description: This function runs a script and returns the ramp up time metric
        based on !{}! aspects of the module

        Example: 
            let metrics = Metrics::new();
            metrics.get_ramp_up();
    */

    pub fn get_ramp_up(&self, module_name: &str) /* -> f64 */ {
        println!("ramp up")
    }

    /* 
        Function: get_correctness
        Arguments: module_name - the name of the module the metric is graded for
        Return: f64 - between 0 and 1

        Description: This function runs a script and returns the correctness metric
        based on !{}! aspects of the module

        Example: 
            let metrics = Metrics::new();
            metrics.get_correctness();
    */

    pub fn get_correctness(&self,  module_name: &str) /* -> f64 */ {
        println!("correctness")
    }


    /* 
        Function: get_bus_factor
        Arguments: module_name - the name of the module the metric is graded for
        Return: f64 - between 0 and 1

        Description: This function runs a script and returns the bus factor metric
        based on !{}! aspects of the module

        Example: 
            let metrics = Metrics::new();
            metrics.get_bus_factor();
    */

    pub fn get_bus_factor(&self,  module_name: &str) /* -> f64 */ {
        println!("bus factor")
    }


    /* 
        Function: get_responsiveness
        Arguments: module_name - the name of the module the metric is graded for
        Return: f64 - between 0 and 1

        Description: This function runs a script and returns the responsiveness metric
        based on !{}! aspects of the module

        Example: 
            let metrics = Metrics::new();
            metrics.get_responsiveness();
    */

    pub fn get_responsiveness(&self,  module_name: &str) /* -> f64 */ {
        println!("responsiveness")
    }


    /* 
        Function: get_license
        Arguments: module_name - the name of the module the metric is graded for
        Return: f64 - between 0 and 1

        Description: This function runs a script and returns the license metric
        based on !{}! aspects of the module

        Example: 
            let metrics = Metrics::new();
            metrics.get_license();
    */


    pub fn get_license(&self,  module_name: &str) /* -> f64 */ {
        println!("license")
    }


    /* 
        Function: get_total
        Arguments: module_name - the name of the module the metric is graded for
        Return: f64 - between 0 and 1

        Description: This function runs an algorithm considering all the metrics calculated above and returns the total grade

        Example: 
            let metrics = Metrics::new();
            metrics.get_total();
    */

    pub fn get_total(&self,  module_name: &str) /* -> f64 */ {
        println!("total")
    }  

    /* 
        Function: get_metrics
        Arguments: module_name - the name of the module the metric is graded for
        Return: None

        Description: This function runs all the scripts and prints the metrics for the module in a tabular format

        Example: 
            let metrics = Metrics::new();
            metrics.get_metrics();
    */

    pub fn get_metrics(&self, module_name: &str) {
        println!("total metrics for {}", module_name);
    }
}