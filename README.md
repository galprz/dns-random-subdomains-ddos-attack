# Dns Random Subdomain DDoS attacks
<p align="center">
  <img src="https://raw.githubusercontent.com/galprz/dns-random-subdomains-ddos-attack/master/images/dns-ddos-attack.png?token=ABX63I2HLZJSGFY7MDLEI6K5UOLHQ"/>
</p>

# Intro
This repository contains implementation for the Mitigating DNS random subdomain DDoS attacks by distinct heavy hitters sketches paper http://www.faculty.idc.ac.il/bremler/Papers/HotWeb_18.pdf [1]

# Setup
First download the code by git clone this repo:
<code>
git clone https://github.com/galprz/dns-random-subdomains-ddos-attack
</code>
Then use conda to install dependencies and setup the environment
<code>
conda end update -f environment.yml
conda activate dns-random-subdomains-ddos-attack 
</code>
# Code structure

+ utils/data.py contains helpers to download the dataset
+ algorithm.py contains the dwsHH and classic heavy hitter algorithm implementation
+ experiment1.ipynb contains the evaluation of the dwsHH as a distinct cardnality estimation
+ experiment2.ipynb contains the evaluation for the end 2 end detection system suggested by the paper
+ report.pdf report that covers [1] and [2]
# Experiments
Google colab links to view notebooks:<br>
experiment 1 - https://colab.research.google.com/drive/1Yk-uiUmInENKCm4NXL1ATxLtmD4bWXad<br>
experiment 2 - https://colab.research.google.com/drive/1uWzWik50PpAt4UqVFQCM8g0TbjJcWCno<br>

# Referances
<code>
@article{1,<br>
	author = {Feibish, Shir Landau and Afek, Yehuda and Bremler-Barr, Anat and Cohen, Edith and Shagam, Michal},<br>
	title = {{Mitigating DNS random subdomain DDoS attacks by distinct heavy hitters sketches}},<br>
	year = {2017},<br>
	month = {Oct},<br>
	isbn = {978-1-4503-5527-8},<br>
	publisher = {ACM},<br>
	doi = {10.1145/3132465.3132474}<br>
}
</code>
<br><br>
<code>
@article{2,<br>
	author = {Chabchoub, Yousra and Chiky, Raja and Dogan, Betul},<br>
	title = {{How can sliding HyperLogLog and EWMA detect port scan attacks in IP traffic?}},<br>
	journal = {EURASIP J. on Info. Security},<br>
	volume = {2014},<br>
	number = {1},<br>
	pages = {1--11},<br>
	year = {2014},<br>
	month = {Dec},<br>
	issn = {1687-417X},<br>
	publisher = {SpringerOpen},<br>
	doi = {10.1186/1687-417X-2014-5}<br>
}
</code>
