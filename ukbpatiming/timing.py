import numpy as np
import pandas as pd

def timing_of_day(df, timing='morning', type_act='MET', morn_hrs=[6, 7, 8, 9, 10, 11],
                  aftn_hrs=[12, 13, 14, 15, 16, 17], even_hrs=[18, 19, 20, 21, 22, 23]):
    if timing == 'morning':
        hours = morn_hrs
    elif timing == 'afternoon':
        hours = aftn_hrs
    elif timing == 'evening':
        hours = even_hrs
    else:
        raise ValueError("Variable timing should be 'morning', 'afternoon', or 'evening'")

    act_daily = np.zeros(df.shape[0])
    for i in hours:
        act_daily += df[f'{type_act}-hourOfDay-{i}-avg']
    df[f'{type_act}_{timing}'] = act_daily

def timing_of_weekday(df, timing='morning', type_act='MET', morn_hrs=[6, 7, 8, 9, 10, 11],
                  aftn_hrs=[12, 13, 14, 15, 16, 17], even_hrs=[18, 19, 20, 21, 22, 23]):
    if timing == 'morning':
        hours = morn_hrs
    elif timing == 'afternoon':
        hours = aftn_hrs
    elif timing == 'evening':
        hours = even_hrs
    else:
        raise ValueError('Variable timing should be \'morning\', \'afternoon\', or \'evening\'')

    act_weekday = np.zeros(df.shape[0])
    for i in hours:
        act_weekday += df[f'{type_act}-hourOfWeekday-{i}-avg']
    df[f'{type_act}_{timing}_weekday'] = act_weekday

def timing_of_weekend(df, timing='morning', type_act='MET', morn_hrs=[6, 7, 8, 9, 10, 11],
                  aftn_hrs=[12, 13, 14, 15, 16, 17], even_hrs=[18, 19, 20, 21, 22, 23]):
    if timing == 'morning':
        hours = morn_hrs
    elif timing == 'afternoon':
        hours = aftn_hrs
    elif timing == 'evening':
        hours = even_hrs
    else:
        raise ValueError('Variable timing should be \'morning\', \'afternoon\', or \'evening\'')

    act_weekend = np.zeros(df.shape[0])
    for i in hours:
        act_weekend += df[f'{type_act}-hourOfWeekend-{i}-avg']
    df[f'{type_act}_{timing}_weekend'] = act_weekend

def time_distribution(df, type_act):
    if f'{type_act}_morning' not in df.columns:
        raise ValueError('Morning activity not available.')
    if f'{type_act}_afternoon' not in df.columns:
        raise ValueError('Afternoon activity not available.')
    if f'{type_act}_evening' not in df.columns:
        raise ValueError('Evening activity not available.')

    morning_prop = df[f'{type_act}_morning']*7/df[f'{type_act}-overall-avg']*7*24
    afternoon_prop = df[f'{type_act}_afternoon']*7/df[f'{type_act}-overall-avg']*7*24
    evening_prop = df[f'{type_act}_evening']*7/df[f'{type_act}-overall-avg']*7*24

    even_dis = [i for i in range(df.shape[0]) if (max(morning_prop[i], afternoon_prop[i], evening_prop[i]) \
                                      - min(morning_prop[i], afternoon_prop[i], evening_prop[i])) < 0.05]
    morning_people = [i for i in range(df.shape[0]) if i not in even_dis and \
                      (max(morning_prop[i], afternoon_prop[i], evening_prop[i])==morning_prop[i])]
    afternoon_people = [i for i in range(df.shape[0]) if i not in even_dis and \
                      (max(morning_prop[i], afternoon_prop[i], evening_prop[i])==afternoon_prop[i])]
    evening_people = [i for i in range(df.shape[0]) if i not in even_dis and \
                      (max(morning_prop[i], afternoon_prop[i], evening_prop[i])==evening_prop[i])]

    df.loc[even_dis,f'{type_act}_distribution'] = 'evenly_distributed'
    df.loc[morning_people, f'{type_act}_distribution'] = 'morning'
    df.loc[afternoon_people, f'{type_act}_distribution'] = 'afternoon'
    df.loc[evening_people, f'{type_act}_distribution'] = 'evening'