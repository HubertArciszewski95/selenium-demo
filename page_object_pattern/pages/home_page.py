class HomePage:
    def __init__(self, driver):
        # Create driver
        self.driver = driver

    # Create page objects

    # Create Methods
    #
    # --- Open page ---
    #
    def open_page(self):
        self.driver.get("http://seleniumdemo.com/")
