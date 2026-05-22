"""Abstract market data provider interface."""

from abc import ABC, abstractmethod


class MarketDataProvider(ABC):
    """Abstract base for market data providers."""

    @abstractmethod
    async def start(self) -> None:
        """Start producing price updates."""

    @abstractmethod
    async def stop(self) -> None:
        """Stop producing price updates."""

    @abstractmethod
    def add_ticker(self, ticker: str) -> None:
        """Start tracking a new ticker."""

    @abstractmethod
    def remove_ticker(self, ticker: str) -> None:
        """Stop tracking a ticker."""
