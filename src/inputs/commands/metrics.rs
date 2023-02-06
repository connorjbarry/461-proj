pub struct Metrics {
    pub ramp_up:f64,
    pub correctness:f64,
    pub bus_factor:f64,
    pub responsiveness:f64,
    pub license:f64,
    pub total:f64,
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
        Arguments: moudule_url - the name of the module the metric is graded for
        Return: f64 - between 0 and 1

        Description: This function runs a script and returns the ramp up time metric
        based on !{}! aspects of the module

        Example: 
            let metrics = Metrics::new();
            metrics.get_ramp_up();
    */

    pub fn get_ramp_up(&mut self, module_url: &str) /* -> f64 */ {
        self.ramp_up = 0.5;
    }

    /* 
        Function: get_correctness
        Arguments: module_url - the name of the module the metric is graded for
        Return: f64 - between 0 and 1

        Description: This function runs a script and returns the correctness metric
        based on !{}! aspects of the module

        Example: 
            let metrics = Metrics::new();
            metrics.get_correctness();
    */

    pub fn get_correctness(&mut self,  module_url: &str) /* -> f64 */ {
        self.correctness = 0.6;
    }


    /* 
        Function: get_bus_factor
        Arguments: module_url - the name of the module the metric is graded for
        Return: f64 - between 0 and 1

        Description: This function runs a script and returns the bus factor metric
        based on !{}! aspects of the module

        Example: 
            let metrics = Metrics::new();
            metrics.get_bus_factor();
    */

    pub fn get_bus_factor(&mut self,  module_url: &str) /* -> f64 */ {
        self.bus_factor = 0.3;
    }


    /* 
        Function: get_responsiveness
        Arguments: module_url - the name of the module the metric is graded for
        Return: f64 - between 0 and 1

        Description: This function runs a script and returns the responsiveness metric
        based on !{}! aspects of the module

        Example: 
            let metrics = Metrics::new();
            metrics.get_responsiveness();
    */

    pub fn get_responsiveness(&mut self,  module_url: &str) /* -> f64 */ {
        self.responsiveness = 0.7;
    }


    /* 
        Function: get_license
        Arguments: module_url - the name of the module the metric is graded for
        Return: f64 - between 0 and 1

        Description: This function runs a script and returns the license metric
        based on !{}! aspects of the module

        Example: 
            let metrics = Metrics::new();
            metrics.get_license();
    */


    pub fn get_license(&mut self,  module_url: &str) /* -> f64 */ {
        self.license =  1.0;
    }


    /* 
        Function: get_total
        Arguments: module_url - the name of the module the metric is graded for
        Return: f64 - between 0 and 1

        Description: This function runs an algorithm considering all the metrics calculated above and returns the total grade

        Example: 
            let metrics = Metrics::new();
            metrics.get_total();
    */

    pub fn get_total(&mut self,  module_url: &str) /* -> f64 */ {
        self.get_ramp_up(module_url);
        self.get_correctness(module_url);
        self.get_bus_factor(module_url);
        self.get_responsiveness(module_url);
        self.get_license(module_url);
        self.total = (self.ramp_up + self.correctness + self.bus_factor + self.responsiveness + self.license) / 5.0;
    }  

    /* 
        Function: get_metrics
        Arguments: module_url - the name of the module the metric is graded for
        Return: None

        Description: This function runs all the scripts and prints the metrics for the module in a tabular format

        Example: 
            let metrics = Metrics::new();
            metrics.get_metrics();
    */

    pub fn get_metrics(&mut self, module_url: &str) {
        self.get_total(module_url);
        println!("{{\"URL\": \"{}\", \"NET_SCORE\": {}, \"RAMP_UP_SCORE\": {}, \"CORRECTNESS_SCORE\": {}, \"BUS_FACTOR_SCORE\": {}, \"RESPONSIVE_MAINTAINER_SCORE\": {}, \"LICENSE_SCORE\": {}}}",
        module_url, self.total, self.ramp_up, self.correctness, self.bus_factor, self.responsiveness, self.license
        );
    }
}