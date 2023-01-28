pub struct Commands {
    install: Option<bool>,
    build: Option<bool>,
    URL: Option<String>,
    test: Option<bool>,
}

impl Commands {
    pub fn new() -> Self {
        Commands {
            install: None,
            build: None,
            URL: None,
            test: None,
        }
    }

    pub fn install(&self) -> Option<bool> {
        self.install
    }

    pub fn build(&self) -> Option<bool> {
        self.build
    }

    pub fn URL(&self) -> Option<String> {
        self.URL.clone()
    }

    pub fn test(&self) -> Option<bool> {
        self.test
    }
}