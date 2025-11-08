# Currency Exchange API 

A lightweight Flask API that retrieves real-time currency exchange rates by scraping data from Wise.com, enabling seamless access to current exchange rate information.

This project is available as a snap package for easy installation on your machine. To customize and rebuild the snap, clone the repository, navigate to the directory containing the `snapcraft.yaml` file, and run:

```bash
snapcraft pack
```

## Installation

To install the snap package, run:
```bash
sudo snap install --dangerous currency-exchange-api_1.0_amd64.snap
```


## Features

- Web form interface on http://localhost:5000/ to query exchange rates
- REST API endpoint for programmatic access
- Integrated web scraper for fetching live exchange rate data
- JSON response format

## Usage
Once snap is installed server will automatically be launched on localhost on port 5000

you can visit the website on your browser by typing "http://localhost:5000/" or by using curl.

```bash
curl -X POST -d "currency_from=USD&currency_to=EGP" http://localhost:5000/currency
```

## Error Handling

If invalid or unsupported currency codes are provided (e.g., not 3 letters or not supported by the web scraper), the API will return an error message like:

```json
{
  "error": "Invalid currency codes or conversion failed: ..."
}
```

## API Endpoints

GET `/`
Returns the HTML form for currency conversion.

Example:
```bash
curl http://localhost:5000/
```

POST `/currency`
Converts between two currencies and returns the exchange rate.

Parameters:
- `currency_from` (required): Source currency code (e.g., USD)
- `currency_to` (required): Target currency code (e.g., EGP)

Response:
```json
{
  "exchange-rate": CURRENT_CURRENCY_RATE
}
```