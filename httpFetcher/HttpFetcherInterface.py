class HttpFetcherInterface:
    def get(self, url: str) -> str:
        """Fetch url, and return html result."""
        pass
