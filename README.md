<p align="center">
  <a href="link-of-our-extension">
    <img alt="GitHub Profile Readme Generator" src="code/extension/images/cheapbuy.png" width="120" />
  </a>
</p>
<h1 align="center">
  cheapBuy
</h1>

---

**cheapBuy Extension** provides you ease to buy any product through your favourite website's like Amazon, Walmart, Ebay, Bjs, Costco, etc, by providing prices of the same product from all different websites to extension. It takes lot of time to search for the same product in different websites, and find the cheapest one, instead just add our extension **cheapBuy** and it will automatically fetch you price of the same product from different websites and you can directly compare the prices from different websites through our extension. In sum, **cheapBuy** is an one stop solution to buy the cheapest product online.

---
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5540375.svg)](https://doi.org/10.5281/zenodo.5540375)
[![codecov](https://codecov.io/gh/aakriti0fnu/cheapBuy/branch/dev_aakriti/graph/badge.svg?token=6D5N39DIO7)](https://codecov.io/gh/aakriti0fnu/cheapBuy)
![github workflow](https://github.com/aakriti0fnu/cheapBuy/actions/workflows/unit_test.yml/badge.svg)
![github workflow](https://github.com/aakriti0fnu/cheapBuy/actions/workflows/style_checker.yml/badge.svg)
![github workflow](https://github.com/aakriti0fnu/cheapBuy/actions/workflows/main.yml/badge.svg)
![github workflow](https://github.com/aakriti0fnu/cheapBuy/actions/workflows/code_cov.yml/badge.svg)
![github workflow](https://github.com/aakriti0fnu/cheapBuy/actions/workflows/close_as_a_feature.yml/badge.svg)
---
<!--Badges-->
<a href="https://github.com/aakriti0fnu/cheapBuy/blob/master/LICENSE" target="blank">
  <img src="https://img.shields.io/github/license/aakriti0fnu/cheapBuy?style=flat-square" alt="cheapBuy license" />
</a>
<a href="https://github.com/aakriti0fnu/cheapBuy/fork" target="blank">
  <img src="https://img.shields.io/github/forks/aakriti0fnu/cheapBuy?style=flat-square" alt="cheapBuy forks" />
</a>
<a href="https://github.com/aakriti0fnu/cheapBuy/stargazers" target="blank">
  <img src="https://img.shields.io/github/stars/aakriti0fnu/cheapBuy?style=flat-square" alt="gcheapBuy stars" />
</a>
<a href="https://github.com/aakriti0fnu/cheapBuy/issues" target="blank">
  <img src="https://img.shields.io/github/issues/aakriti0fnu/cheapBuy?style=flat-square" alt="cheapBuy issues" />
</a>
<a href="https://github.com/aakriti0fnu/cheapBuy/issues" target="blank">
  <img src="https://img.shields.io/github/issues-closed/aakriti0fnu/cheapBuy" alt="cheapBuy issues closed" />
</a>
<a href="https://github.com/aakriti0fnu/cheapBuy/pulls" target="blank">
  <img src="https://img.shields.io/github/issues-pr/aakriti0fnu/cheapBuy?style=flat-square" alt="cheapBuy pull-requests" />
</a>
<a href="https://github.com/aakriti0fnu/cheapBuy/graphs/contributors" alt="Contributors">
  <img src="https://img.shields.io/github/contributors/aakriti0fnu/cheapBuy" />
</a>
<a href="https://github.com/aakriti0fnu/cheapBuy/milestones" alt="milestones">
  <img src="https://img.shields.io/github/milestones/all/aakriti0fnu/cheapBuy" />
</a>
<a href="https://github.com/aakriti0fnu/cheapBuy/graphs/commit-activity" alt="commit activity">
  <img src="https://img.shields.io/github/commit-activity/w/aakriti0fnu/cheapBuy" />
</a>
<a href="https://github.com/aakriti0fnu/cheapBuy/discussions" alt="discussion">
  <img src="https://img.shields.io/github/discussions/aakriti0fnu/cheapBuy" />
</a>
<a href="https://img.shields.io/github/repo-size/aakriti0fnu/cheapBuy" alt="repo size">
  <img src="https://img.shields.io/github/repo-size/aakriti0fnu/cheapBuy" />
</a>
<a href="https://img.shields.io/tokei/lines/github/aakriti0fnu/cheapBuy" alt="total lines">
  <img src="https://img.shields.io/tokei/lines/github/aakriti0fnu/cheapBuy" />
</a>

----
<p align="center">
    <a href="https://github.com/aakriti0fnu/cheapBuy/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/aakriti0fnu/cheapBuy/issues/new/choose">Request Feature</a>
</p>

----
## 🚀 Demo 

[![cheapBuy Extension](https://img.youtube.com/vi/Rd5pno8FuD4/0.jpg)](https://www.youtube.com/watch?v=Rd5pno8FuD4)
## 🧐 Features
- **Price Comparison**
- **Get alternative website for the product**


## 🛠️ Installation Steps

---
1. Clone this github repository at the preferable location in your system. You will need [git](https://git-scm.com/downloads) to be pre-installed in your system.
    ```
    git clone https://github.com/aakriti0fnu/cheapBuy.git
    cd cheapBuy
    ```
2. This project uses Python3(`tested with >3.8 version`), so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are pre-installed.
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
4. Check out the demo video to know about the use of the extension.

## How to run it locally?
- Run the server. 
    ```
    python code/web/server_api.py
    ```
- upload the extension into your browser of choice(`tested on chrome.`)
  - go to `chrome` browser's settings
  - select `Extensions`
  - select `Load unpacked`
  - select folder [extension](./code/extension)
  Now, it's visible in your browser.
- Choose a website of your choice among these [Amazon, ebay, bjs, Walmart, Costco] for an item.
- Once you've selected the item on a site, click on the extension icon and wait for a few seconds to see the suggestions.

    
## Plan of Action :

<details open>
<summary>PHASE-1: </summary>
<br>
<ul>
<li>  Fetching description of the user's current tab for ebay. </li>
<li>  Fetching description of the user's current tab for Walmart. </li>
<li>  Fetching description of the user's current tab for amazon. </li>
<li>  Fetching description of the user's current tab for Bjs. </li>
<li>  Fetching description of the user's current tab for Costco. </li>
<li>  Web Scrapping various product details from amazon. </li>
<li>  Web Scrapping various product details from Ebay. </li>
<li>  Exception handling of web scrapping. </li>
<li>  Server API for web scrapping. </li>
<li>  Deploying server on AWS. </li>
<li>  Build an extension for this price comparison. </li>
<li>  Extract knowledge like prices, sites, URL, comparison, description from scrapped data. </li>
<li>  Show all the scrapped data and the knowledge gained on the extension page. </li>
</ul>
</details>

<details open>
<summary>PHASE-2 :</summary>
<br>
<ul>
<li> Add a badge on the user's current tab. </li>
<li> Improvement of extension UI. </li>
<li> Alternate product suggestion feature. </li>
<li> Improve accuracy of the product. Example : If user's current tab is having Television of a particular brand and there is a better option available at a cheaper or comparable rate than provide alternative product accordingly. </li>
<li> Add web scrapping for other websites such as Walmart, Bjs, Costco, etc. </li>
<li> Improve code execution speed using multithreading. </li>
<li> Show a avialable coupon on other shopping website. </li>
</ul>
</details>

<details open>
<summary>PHASE-3 :</summary>
<br>
<ul>
<li> Automatic deployment of server using Teraform or ansible. </li>
<li> Develop a website instead of extension. </li>
<li> Dashboard including how many user's click on the website. </li>
<li> Email notification of the available coupon to the user. </li>
</ul>
</details>

🌟 You are all set!

## 🍰 Contributing
Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/het=patel99/cheapBuy/compare).

Please read [`CONTRIBUTING`](CONTRIBUTING.md) for details on our [`CODE OF CONDUCT`](CODE_OF_CONDUCT.md), and the process for submitting pull requests to us.

## Contributors

- [Aakriti](https://github.com/aakriti0fnu)
- [AshwinKumarMuniswamy](https://github.com/AshwinKumarMuniswamy)
- [Jainam Shah](https://github.com/j-08-shah)
- [Sharath Kumar](https://github.com/sharathKV)
