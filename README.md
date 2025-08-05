# Pratik's Ethereum Transaction Dashboard

An advanced, interactive dashboard built with Python and Streamlit to view, analyze, and track live transactions for any public Ethereum wallet address. This tool provides deep insights into on-chain activity through a clean, modern, and user-friendly interface.

# Pratik's Ethereum Transaction Dashboard

![Ethereum Dashboard Preview](https://iili.io/FPGCCxt.png)

An advanced, interactive dashboard built with Python and Streamlit...


## ✨ Features

* **Live Transaction Feed**: Enable live mode to automatically refresh and display new transactions every 15 seconds.
* **Comprehensive Analytics**: View key metrics like total transactions, total ETH received/sent, and average gas fees over time.
* **Rich Visualizations**: Interactive charts for transaction volume, gas prices, and top sender/receiver addresses.
* **Bilingual Support**: Seamlessly switch between English and Hindi (Rowdy) language options.
* **Modern UI/UX**: A clean, animated, and responsive interface that works on both desktop and mobile.
* **Detailed Transaction Table**: A styled and easy-to-read table showing the most recent 100 transactions with links to Etherscan.

## 🚀 How to Run Locally

Follow these steps to get the dashboard running on your own machine.

### Prerequisites

* Python 3.8 or higher
* An Etherscan API Key (you can get a free one [here](https://etherscan.io/myapikey))

### Installation & Setup

1.  **Clone the repository:**
    Open your terminal and run the following command to clone the project files.
    ```bash
    git clone [https://github.com/Pratik03538/ethereum-dashboard.git](https://github.com/Pratik03538/ethereum-dashboard.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd ethereum-dashboard
    ```

3.  **Install the required libraries:**
    This command will automatically install all the necessary Python libraries listed in the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    This command will start the application. Your web browser should automatically open with the dashboard.
    ```bash
    streamlit run app.py
    ```

5.  **Use the Dashboard:**
    * Enter your Etherscan API Key and the desired Ethereum wallet address in the sidebar.
    * Click "Fetch Initial Transactions" to load the data.

## 🛠️ Built With

* [**Streamlit**](https://streamlit.io/) - The core framework for building the interactive web app.
* [**Pandas**](https://pandas.pydata.org/) - For data manipulation and analysis.
* [**Plotly**](https://plotly.com/) - For creating interactive charts and visualizations.
* [**Requests**](https://requests.readthedocs.io/en/latest/) - For making API calls to the Etherscan API.
* [**Etherscan API**](https://etherscan.io/apis) - The data source for all Ethereum blockchain information.
