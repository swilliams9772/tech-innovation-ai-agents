class DataIntegrator:
    def __init__(self, data_sources):
        self.data_sources = data_sources
        self.cache = {}
        
    def integrate_data(self, query):
        """Integrate data from multiple sources"""
        results = []
        for source in self.data_sources:
            data = source.query(query)
            cleaned_data = self.clean_data(data)
            results.append(cleaned_data)
        return self.merge_results(results) 