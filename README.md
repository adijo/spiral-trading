# Spiral Trading #
[ ![Codeship Status for adijo/spiral-trading](https://codeship.com/projects/aa4cbdb0-ffe5-0133-e044-66a4d3edd024/status?branch=master)](https://codeship.com/projects/152976)

## Quick summary

This is an algorithmic trading platform designed to live in the cloud and automatically carry out trades in the Indian stock market. It is intended to be fully automated using various quantitative trading tools. The scope is to initially manage some of my personal capital, and if it does well, start offering it out as a mini hedge fund / service to whoever is interested in purchasing it.

## Plan

* The architecture should be such that any model or strategy can be plugged in without disturbing any other component. The notification section will currently be Slack and Email, although Slack would be the first one to be rolled out.
* The next part would be to incorporate Zipline, which is the back-end for back testing and algorithm development for Quantopian.

## Setup
* Edit the `PYTHONPATH` variable before launching the project

## Project Structure

### Strategies
* The trades will be executed with a number of strategies specified in the `strategies` folder. Currently, we will be using a simple mean reversion with rolling mean strategy as described [here.](https://www.quantopian.com/posts/bollinger-bands-with-trading)
* A `strategy` has the following responsibilities:
    1. As inputs, it receives a file which contains a list of all the `symbols` that it should look at, the `exchange,` for which it should trade and a `dictionary` of strategy specific properties. 
    2. Whenever it is run, it should return a `plan.`
    3. A `plan` is defined simply as a list of dictionaries where each dictionary corresponds to a trade order. Example: 
      ```{tradingsymbol:"INFY",
                    exchange:"NSE",
                    transaction_type:"BUY",
                    quantity:1,
                    order_type:"MARKET",
                    product:"NRML"}```