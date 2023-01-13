# Timing of Device-Measured Physical Activity from UK Biobank

This is a tool to get information about how much exercise people perform during the morning, afternoon and evening based on accelerometer-measured data from UK Biobank. The input should be pre-processed raw data with biobank Accelerometer Analysis. For more detail, see https://github.com/OxWearables/biobankAccelerometerAnalysis.

## Installation

```css
pip install ukbpatiming
```
## Usage

This tool enables PA average computing over the whole measurement period, weekday only and weekend only. Timing of morning, afternoon, and evening can be manually specified.

### Compute timing of PA in terms of MET hours
Here we use the default hours setting: morning 6am-12pm, afternoon 12pm-6pm, evening 6pmm-12pm. You may change this by passing different parameters. For example, if you would like to specify morning to be 5am-12pm, you may change to `morn_hrs = [5,6,7,8,9,10,11]`.

Make sure the column `{type_act}-hourOfDay-{hour}-avg` is available in your dataframe.

```css
from ukbpatiming.timing import timing_of_day
timing_of_day(df, timing='morning', type_act='MET', morn_hrs=[6, 7, 8, 9, 10, 11],
              aftn_hrs=[12, 13, 14, 15, 16, 17], even_hrs=[18, 19, 20, 21, 22, 23])
```

### Categorize people into groups
Categorize people into morning, afternoon, evening, or evenly_distributed groups based on how many hours they perform activities during the time range. If they perform the most in the morning, then they are categorized as a morning person.

Make sure `{type_act}-overall-avg` is available in your dataframe to specify the total average time of exercising in an hour, e.g. 0.3 hours per hour per day, which means 0.3*7*24 hours per week.

```css
from ukbpatiming.timing import time_distribution
time_distribution(df, 'MET')
```

### Other cases
`timing_of_weekday` and `timing_of_weekend` are available to calculate the average PA in a time range over the weekdays or weekend. Other PA measurement, e.g. MVPA, VPA, can also be applied. See more details in `example.ipynb`.