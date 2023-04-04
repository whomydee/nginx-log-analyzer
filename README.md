# nginx-log-analyzer

nginx log analyzer provide you some features to analyze the access log for nginx, for instance - getting the list of IP address that accessed your site within a specific timeframe, the highest number of hits that came within a timeframe that is specifed by you.

In one Sentence - it helps you to know if your site is in or has been in DDos Attacks or not in addition with many things.
## Features

- Access Summary within a specified timeframe
- Highest Number of hits that Came from a timeframe
- The status codes that if the requests that reached
## Run Locally

Clone the project

```bash
  git clone https://github.com/whomydee/nginx-log-analyzer
```

Go to the project directory

```bash
  cd nginx-log-analyzer
```

Install dependencies

```bash
  python3 -m pip install -r requirements.txt
```

Run the script (It will print the whole summary. Please refer to the usage below for more details on how to use it.)

```bash
  python run.py
```
For the First time Run it will ask you to give the location of your access log file. Provide the location, from next
time no need to input this location. (PS- This is configurable, you can use the **--file-location** switch to use another
file for analysis. )

```bash
Please enter the location of the file:
~/Desktop/my_access.log
```
## Usage / Examples

### The Highest Hits for a Specific Time Interval

This fetches the maximum hit that came to your site within the specific time range. Here I used --time-interval 10; it 
means I want to see all the hits that came within that timeframe by a 10 minutes interval. I also used --topk 3;
meaning it will bring me the latest top 3 results that matches that criteria.

```bash
$ python run.py --start-time 15/Mar/2023:12:00:00 --end-time 15/Mar/2023:17:35:00 --time-interval 10 --topk 3
```

### Full Summary of the Access Log

```bash
$ python run.py
```

### Access Summary within a Specified Timeframe

```bash
$ python run.py --start-time 15/Mar/2023:12:00:00 --end-time 15/Mar/2023:17:35:00
```
If you want to see **only the IPs** with a **minimum hit** count of **15** (change as your deem fit).

```bash
$ python run.py --start-time 15/Mar/2023:12:00:00 --end-time 15/Mar/2023:17:35:00 --min-hit-count 15
```

If you want to see **only the IPs** that **hit minimum 15 times** with the **Timestamp**** when those hit took place

```bash
$ python run.py --min-hit-count 15 --timestamp True
```

If you want to see **only the IPs** that hit minimum 15 times with the **Timestamp** and **Status Code**

```bash
$ python run.py --min-hit-count 15 --timestamp True --status-code-wise True
```
## Demo

Here are some demos of nginx-log-analyzer in action:

![Alt Text](https://github.com/whomydee/nginx-log-analyzer/blob/main/assets/demo-1.gif)


![Alt Text](https://github.com/whomydee/nginx-log-analyzer/blob/main/assets/demo-2.gif)


## License

[MIT](https://choosealicense.com/licenses/mit/)


## 🚀 About Me
I'm Shad, a Software Engineer in AI/ML who happens to love the DevOps and Architecture side of the Applications.

I currently work in Infolytx (infolytx.com) as a Software Engineer II in AI/ML/Architecture 

