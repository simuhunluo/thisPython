# -*-encoding=utf-8-*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
testdata = pd.read_csv("K:\\thisPython\python\lesson7_experiment_skycat_feature+\\feature_temp.csv")
test_feature_data = testdata[(testdata.visit_datetime >= '2013/5/15')
                               & (testdata.visit_datetime <= '2013/7/15')]
test_label_data = testdata[(testdata.visit_datetime >= '2013/7/16')
                             & (testdata.visit_datetime <= '2013/8/15')]
user_id_test_feature_data = test_feature_data.iloc[:, [0, 2, 3]]
# 用户 1天 点击（标记0）
user_id_test_feature_data_1 = user_id_test_feature_data[user_id_test_feature_data.visit_datetime == '2013/7/15']
user_id_test_feature_data_1 = user_id_test_feature_data_1.iloc[:, [0, 1]]
user_id_test_feature_data_1_click = user_id_test_feature_data_1[user_id_test_feature_data_1.type == 0]
# 用户 1天 购买（标记1）
user_id_test_feature_data_1_buy = user_id_test_feature_data_1[user_id_test_feature_data_1.type == 1]
# 用户 1天 收藏（标记2）
user_id_test_feature_data_1_collect = user_id_test_feature_data_1[
    user_id_test_feature_data_1.type == 2]
# 用户 1天 加入购物车（标记3）
user_id_test_feature_data_1_cart = user_id_test_feature_data_1[
    user_id_test_feature_data_1.type == 3]

user_id_test_feature_data_7 = user_id_test_feature_data[
    (user_id_test_feature_data.visit_datetime <= '2013/7/15')
    &
    (user_id_test_feature_data.visit_datetime >= '2013/7/9')
    ]
user_id_test_feature_data_7 = user_id_test_feature_data_7.iloc[:, [0, 1]]
# 用户 7天 点击（标记0）
user_id_test_feature_data_7_click = user_id_test_feature_data_7[user_id_test_feature_data_7.type == 0]
# 用户 7天 购买（标记1）
user_id_test_feature_data_7_buy = user_id_test_feature_data_7[user_id_test_feature_data_7.type == 1]
# 用户 7天 收藏（标记2）
user_id_test_feature_data_7_collect = user_id_test_feature_data_7[
    user_id_test_feature_data_7.type == 2]
# 用户 7天 加入购物车（标记3）
user_id_test_feature_data_7_cart = user_id_test_feature_data_7[
    user_id_test_feature_data_7.type == 3]

user_id_test_feature_data_14 = user_id_test_feature_data[
    (user_id_test_feature_data.visit_datetime <= '2013/7/15')
    &
    (user_id_test_feature_data.visit_datetime >= '2013/7/2')
    ]
user_id_test_feature_data_14 = user_id_test_feature_data_14.iloc[:, [0, 1]]
# 用户 14天 点击（标记0）
user_id_test_feature_data_14_click = user_id_test_feature_data_14[user_id_test_feature_data_14.type == 0]
# 用户 14天 购买（标记1）
user_id_test_feature_data_14_buy = user_id_test_feature_data_14[user_id_test_feature_data_14.type == 1]
# 用户 14天 收藏（标记2）
user_id_test_feature_data_14_collect = user_id_test_feature_data_14[
    user_id_test_feature_data_14.type == 2]
# 用户 14天 加入购物车（标记3）
user_id_test_feature_data_14_cart = user_id_test_feature_data_14[
    user_id_test_feature_data_14.type == 3]

user_id_test_feature_data_28 = user_id_test_feature_data[
    (user_id_test_feature_data.visit_datetime <= '2013/7/15')
    &
    (user_id_test_feature_data.visit_datetime >= '2013/6/18')
    ]
user_id_test_feature_data_28 = user_id_test_feature_data_28.iloc[:, [0, 1]]
# 用户 28天 点击（标记0）
user_id_test_feature_data_28_click = user_id_test_feature_data_28[user_id_test_feature_data_28.type == 0]
# 用户 28天 购买（标记1）
user_id_test_feature_data_28_buy = user_id_test_feature_data_28[user_id_test_feature_data_28.type == 1]
# 用户 28天 收藏（标记2）
user_id_test_feature_data_28_collect = user_id_test_feature_data_28[
    user_id_test_feature_data_28.type == 2]
# 用户 28天 加入购物车（标记3）
user_id_test_feature_data_28_cart = user_id_test_feature_data_28[
    user_id_test_feature_data_28.type == 3]


brand_id_test_feature_data = test_feature_data.iloc[:, [1, 2, 3]]
# 品牌 1天 点击（标记0）
brand_id_test_feature_data_1 = brand_id_test_feature_data[brand_id_test_feature_data.visit_datetime == '2013/7/15']
brand_id_test_feature_data_1=brand_id_test_feature_data_1.iloc[:,[0,1]]
brand_id_test_feature_data_1_click=brand_id_test_feature_data_1[brand_id_test_feature_data_1.type==0]
# 品牌 1天 购买（标记1）
brand_id_test_feature_data_1_buy = brand_id_test_feature_data_1[brand_id_test_feature_data_1.type == 1]
# 品牌 1天 收藏（标记2）
brand_id_test_feature_data_1_collect = brand_id_test_feature_data_1[
    brand_id_test_feature_data_1.type == 2]
# 品牌 1天 加入购物车（标记3）
brand_id_test_feature_data_1_cart = brand_id_test_feature_data_1[
    brand_id_test_feature_data_1.type == 3]

brand_id_test_feature_data_7 = brand_id_test_feature_data[
    (brand_id_test_feature_data.visit_datetime <= '2013/7/15' )
    &
    (brand_id_test_feature_data.visit_datetime >= '2013/7/9')
]
brand_id_test_feature_data_7=brand_id_test_feature_data_7.iloc[:,[0,1]]
# 品牌 7天 点击（标记0）
brand_id_test_feature_data_7_click=brand_id_test_feature_data_7[brand_id_test_feature_data_7.type==0]
# 品牌 7天 购买（标记1）
brand_id_test_feature_data_7_buy = brand_id_test_feature_data_7[brand_id_test_feature_data_7.type == 1]
# 品牌 7天 收藏（标记2）
brand_id_test_feature_data_7_collect = brand_id_test_feature_data_7[
    brand_id_test_feature_data_7.type == 2]
# 品牌 7天 加入购物车（标记3）
brand_id_test_feature_data_7_cart = brand_id_test_feature_data_7[
    brand_id_test_feature_data_7.type == 3]

brand_id_test_feature_data_14 = brand_id_test_feature_data[
    (brand_id_test_feature_data.visit_datetime <= '2013/7/15' )
    &
    (brand_id_test_feature_data.visit_datetime >= '2013/7/2')
]
brand_id_test_feature_data_14=brand_id_test_feature_data_14.iloc[:,[0,1]]
# 品牌 14天 点击（标记0）
brand_id_test_feature_data_14_click=brand_id_test_feature_data_14[brand_id_test_feature_data_14.type==0]
# 品牌 14天 购买（标记1）
brand_id_test_feature_data_14_buy = brand_id_test_feature_data_14[brand_id_test_feature_data_14.type == 1]
# 品牌 14天 收藏（标记2）
brand_id_test_feature_data_14_collect = brand_id_test_feature_data_14[
    brand_id_test_feature_data_14.type == 2]
# 品牌 14天 加入购物车（标记3）
brand_id_test_feature_data_14_cart = brand_id_test_feature_data_14[
    brand_id_test_feature_data_14.type == 3]

brand_id_test_feature_data_28 = brand_id_test_feature_data[
    (brand_id_test_feature_data.visit_datetime <= '2013/7/15' )
    &
    (brand_id_test_feature_data.visit_datetime >= '2013/6/18')
]
brand_id_test_feature_data_28=brand_id_test_feature_data_28.iloc[:,[0,1]]
# 品牌 28天 点击（标记0）
brand_id_test_feature_data_28_click=brand_id_test_feature_data_28[brand_id_test_feature_data_28.type==0]
# 品牌 28天 购买（标记1）
brand_id_test_feature_data_28_buy = brand_id_test_feature_data_28[brand_id_test_feature_data_28.type == 1]
# 品牌 28天 收藏（标记2）
brand_id_test_feature_data_28_collect = brand_id_test_feature_data_28[
    brand_id_test_feature_data_28.type == 2]
# 品牌 28天 加入购物车（标记3）
brand_id_test_feature_data_28_cart = brand_id_test_feature_data_28[
    brand_id_test_feature_data_28.type == 3]

user_brand_test_feature_data = test_feature_data
# 用户&品牌 1天 点击（标记0）
user_brand_test_feature_data_1 = user_brand_test_feature_data[
    user_brand_test_feature_data.visit_datetime == '2013/7/15']
user_brand_test_feature_data_1 = user_brand_test_feature_data_1.iloc[:, [0, 1, 2]]

user_brand_test_feature_data_1_click = user_brand_test_feature_data_1[user_brand_test_feature_data_1.type == 0]

# 用户&品牌 1天 购买（标记1）
user_brand_test_feature_data_1_buy = user_brand_test_feature_data_1[user_brand_test_feature_data_1.type == 1]
# 用户&品牌 1天 收藏（标记2）
user_brand_test_feature_data_1_collect = user_brand_test_feature_data_1[
    user_brand_test_feature_data_1.type == 2]
# 用户&品牌 1天 加入购物车（标记3）
user_brand_test_feature_data_1_cart = user_brand_test_feature_data_1[
    user_brand_test_feature_data_1.type == 3]

user_brand_test_feature_data_7 = user_brand_test_feature_data[
    (user_brand_test_feature_data.visit_datetime <= '2013/7/15')
    &
    (user_brand_test_feature_data.visit_datetime >= '2013/7/9')
    ]
user_brand_test_feature_data_7 = user_brand_test_feature_data_7.iloc[:, [0, 1, 2]]
# 用户&品牌 7天 点击（标记0）
user_brand_test_feature_data_7_click = user_brand_test_feature_data_7[user_brand_test_feature_data_7.type == 0]
# 用户&品牌 7天 购买（标记1）
user_brand_test_feature_data_7_buy = user_brand_test_feature_data_7[user_brand_test_feature_data_7.type == 1]
# 用户&品牌 7天 收藏（标记2）
user_brand_test_feature_data_7_collect = user_brand_test_feature_data_7[
    user_brand_test_feature_data_7.type == 2]
# 用户&品牌 7天 加入购物车（标记3）
user_brand_test_feature_data_7_cart = user_brand_test_feature_data_7[
    user_brand_test_feature_data_7.type == 3]

user_brand_test_feature_data_14 = user_brand_test_feature_data[
    (user_brand_test_feature_data.visit_datetime <= '2013/7/15')
    &
    (user_brand_test_feature_data.visit_datetime >= '2013/7/2')
    ]
user_brand_test_feature_data_14 = user_brand_test_feature_data_14.iloc[:, [0, 1, 2]]
# 用户&品牌 14天 点击（标记0）
user_brand_test_feature_data_14_click = user_brand_test_feature_data_14[user_brand_test_feature_data_14.type == 0]
# 用户&品牌 14天 购买（标记1）
user_brand_test_feature_data_14_buy = user_brand_test_feature_data_14[user_brand_test_feature_data_14.type == 1]
# 用户&品牌 14天 收藏（标记2）
user_brand_test_feature_data_14_collect = user_brand_test_feature_data_14[
    user_brand_test_feature_data_14.type == 2]
# 用户&品牌 14天 加入购物车（标记3）
user_brand_test_feature_data_14_cart = user_brand_test_feature_data_14[
    user_brand_test_feature_data_14.type == 3]

user_brand_test_feature_data_28 = user_brand_test_feature_data[
    (user_brand_test_feature_data.visit_datetime <= '2013/7/15')
    &
    (user_brand_test_feature_data.visit_datetime >= '2013/6/18')
    ]
user_brand_test_feature_data_28 = user_brand_test_feature_data_28.iloc[:, [0, 1, 2]]
# 用户&品牌 28天 点击（标记0）
user_brand_test_feature_data_28_click = user_brand_test_feature_data_28[user_brand_test_feature_data_28.type == 0]
# 用户&品牌 28天 购买（标记1）
user_brand_test_feature_data_28_buy = user_brand_test_feature_data_28[user_brand_test_feature_data_28.type == 1]
# 用户&品牌 28天 收藏（标记2）
user_brand_test_feature_data_28_collect = user_brand_test_feature_data_28[
    user_brand_test_feature_data_28.type == 2]
# 用户&品牌 28天 加入购物车（标记3）
user_brand_test_feature_data_28_cart = user_brand_test_feature_data_28[
    user_brand_test_feature_data_28.type == 3]

# 用户 60天 点击变购率（60天中点击数中有多少个购买的）
user_id_test_feature_data = test_feature_data.iloc[:, [0, 2, 3]]
user_id_test_feature_data_60 = user_id_test_feature_data[
    (user_id_test_feature_data.visit_datetime <= '2013/7/15')
    &
    (user_id_test_feature_data.visit_datetime >= '2013/5/17')
    ]
user_id_test_feature_data_60=user_id_test_feature_data_60.iloc[:,[0,1]]
# 用户 60天 点击（标记0）
user_id_test_feature_data_60_click = user_id_test_feature_data_60[
    user_id_test_feature_data_60.type == 0]
# 用户 60天 购买（标记1）
user_id_test_feature_data_60_buy = user_id_test_feature_data_60[
    user_id_test_feature_data_60.type == 1]
click_count_60 = user_id_test_feature_data_60_click.groupby(['user_id'], as_index=False)["type"].agg(
    {"user_clickCount": "count"})
buy_count_60 = user_id_test_feature_data_60_buy.groupby(['user_id'], as_index=False)["type"].agg(
    {"user_buyCount": "count"})
tmp = pd.merge(click_count_60, buy_count_60, how="outer")
tmp = tmp.fillna(0)
tmp["user_rate_buyOfClick"] = tmp['user_buyCount'] / tmp['user_clickCount']
tmp = tmp.round(4)
user_rate_buyOfClick = tmp.iloc[:, [0, 3]]

# 用户 60天 收藏变购率（60天中收藏数中有多少个购买的）
# 用户 60天 收藏（标记2）
user_id_test_feature_data_60_collect = user_id_test_feature_data_60[
    user_id_test_feature_data_60.type == 2]
# 用户 60天 购买（标记1）
user_id_test_feature_data_60_buy = user_id_test_feature_data_60[
    user_id_test_feature_data_60.type == 1]
collect_count_60 = user_id_test_feature_data_60_collect.groupby(['user_id'], as_index=False)["type"].agg(
    {"user_collectCount": "count"})
buy_count_60 = user_id_test_feature_data_60_buy.groupby(['user_id'], as_index=False)["type"].agg(
    {"user_buyCount": "count"})
tmp = pd.merge(collect_count_60, buy_count_60, how="outer")
tmp = tmp.fillna(0)
tmp["user_rate_buyOfCollect"] = tmp['user_buyCount'] / tmp['user_collectCount']
tmp = tmp.round(4)
user_rate_buyOfCollect = tmp.iloc[:, [0, 3]]

# 用户 60天 加购变购率（60天中加购数中有多少个购买的）
# 用户 60天 加购（标记3）
user_id_test_feature_data_60_cart = user_id_test_feature_data_60[
    user_id_test_feature_data_60.type == 3]
# 用户 60天 购买（标记1）
user_id_test_feature_data_60_buy = user_id_test_feature_data_60[
    user_id_test_feature_data_60.type == 1]
cart_count_60 = user_id_test_feature_data_60_cart.groupby(['user_id'], as_index=False)["type"].agg(
    {"user_cartCount": "count"})
buy_count_60 = user_id_test_feature_data_60_buy.groupby(['user_id'], as_index=False)["type"].agg(
    {"user_buyCount": "count"})
tmp = pd.merge(cart_count_60, buy_count_60, how="outer")
tmp = tmp.fillna(0)
tmp["user_rate_buyOfCart"] = tmp['user_buyCount'] / tmp['user_cartCount']
tmp = tmp.round(4)
user_rate_buyOfCart = tmp.iloc[:, [0, 3]]

# 品牌 60天 点击变购率（60天中点击数中有多少个购买的）
brand_id_test_feature_data = test_feature_data.iloc[:, [1, 2, 3]]
brand_id_test_feature_data_60 = brand_id_test_feature_data[
    (brand_id_test_feature_data.visit_datetime <= '2013/7/15')
    &
    (brand_id_test_feature_data.visit_datetime >= '2013/5/17')
    ]
brand_id_test_feature_data_60=brand_id_test_feature_data_60.iloc[:,[0,1]]
# 品牌 60天 点击（标记0）
brand_id_test_feature_data_60_click = brand_id_test_feature_data_60[
    brand_id_test_feature_data_60.type == 0]
# 品牌 60天 购买（标记1）
brand_id_test_feature_data_60_buy = brand_id_test_feature_data_60[
    brand_id_test_feature_data_60.type == 1]
click_count_60 = brand_id_test_feature_data_60_click.groupby(['brand_id'], as_index=False)["type"].agg(
    {"brand_clickCount": "count"})
buy_count_60 = brand_id_test_feature_data_60_buy.groupby(['brand_id'], as_index=False)["type"].agg(
    {"brand_buyCount": "count"})
tmp = pd.merge(click_count_60, buy_count_60, how="outer")
tmp = tmp.fillna(0)
tmp["brand_rate_buyOfClick"] = tmp['brand_buyCount'] / tmp['brand_clickCount']
tmp = tmp.round(4)
brand_rate_buyOfClick = tmp.iloc[:, [0, 3]]

# 品牌 60天 收藏变购率（60天中收藏数中有多少个购买的）
# 品牌 60天 收藏（标记2）
brand_id_test_feature_data_60_collect = brand_id_test_feature_data_60[
    brand_id_test_feature_data_60.type == 2]
# 品牌 60天 购买（标记1）
brand_id_test_feature_data_60_buy = brand_id_test_feature_data_60[
    brand_id_test_feature_data_60.type == 1]
collect_count_60 = brand_id_test_feature_data_60_collect.groupby(['brand_id'], as_index=False)["type"].agg(
    {"brand_collectCount": "count"})
buy_count_60 = brand_id_test_feature_data_60_buy.groupby(['brand_id'], as_index=False)["type"].agg(
    {"brand_buyCount": "count"})
tmp = pd.merge(collect_count_60, buy_count_60, how="outer")
tmp = tmp.fillna(0)
tmp["brand_rate_buyOfCollect"] = tmp['brand_buyCount'] / tmp['brand_collectCount']
tmp = tmp.round(4)
brand_rate_buyOfCollect = tmp.iloc[:, [0, 3]]

# 品牌 60天 加购变购率（60天中加购数中有多少个购买的）
# 品牌 60天 加购（标记3）
brand_id_test_feature_data_60_cart = brand_id_test_feature_data_60[
    brand_id_test_feature_data_60.type == 3]
# 品牌 60天 购买（标记1）
brand_id_test_feature_data_60_buy = brand_id_test_feature_data_60[
    brand_id_test_feature_data_60.type == 1]
cart_count_60 = brand_id_test_feature_data_60_cart.groupby(['brand_id'], as_index=False)["type"].agg(
    {"brand_cartCount": "count"})
buy_count_60 = brand_id_test_feature_data_60_buy.groupby(['brand_id'], as_index=False)["type"].agg(
    {"brand_buyCount": "count"})
tmp = pd.merge(cart_count_60, buy_count_60, how="outer")
tmp = tmp.fillna(0)
tmp["brand_rate_buyOfCart"] = tmp['brand_buyCount'] / tmp['brand_cartCount']
tmp = tmp.round(4)
brand_rate_buyOfCart = tmp.iloc[:, [0, 3]]

#要统计了  先统计再 重命名
#用户 1天
user_id_test_feature_data_1_clickCount\
    = user_id_test_feature_data_1_click.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_1_clickCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_1_buyCount\
    = user_id_test_feature_data_1_buy.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_1_buyCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_1_collectCount\
    = user_id_test_feature_data_1_collect.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_1_collectCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_1_cartCount\
    = user_id_test_feature_data_1_cart.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_1_cartCount":"count"}).iloc[:,[0,1]]

#用户 7天
user_id_test_feature_data_7_clickCount\
    = user_id_test_feature_data_7_click.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_7_clickCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_7_buyCount\
    = user_id_test_feature_data_7_buy.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_7_buyCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_7_collectCount\
    = user_id_test_feature_data_7_collect.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_7_collectCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_7_cartCount\
    = user_id_test_feature_data_7_cart.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_7_cartCount":"count"}).iloc[:,[0,1]]
#用户 14天
user_id_test_feature_data_14_clickCount\
    = user_id_test_feature_data_14_click.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_14_clickCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_14_buyCount\
    = user_id_test_feature_data_14_buy.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_14_buyCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_14_collectCount\
    = user_id_test_feature_data_14_collect.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_14_collectCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_14_cartCount\
    = user_id_test_feature_data_14_cart.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_14_cartCount":"count"}).iloc[:,[0,1]]
#用户 28天
user_id_test_feature_data_28_clickCount\
    = user_id_test_feature_data_28_click.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_28_clickCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_28_buyCount\
    = user_id_test_feature_data_28_buy.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_28_buyCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_28_collectCount\
    = user_id_test_feature_data_28_collect.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_28_collectCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_28_cartCount\
    = user_id_test_feature_data_28_cart.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_28_cartCount":"count"}).iloc[:,[0,1]]

#品牌 1天
brand_id_test_feature_data_1_clickCount\
    = brand_id_test_feature_data_1_click.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_1_clickCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_1_buyCount\
    = brand_id_test_feature_data_1_buy.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_1_buyCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_1_collectCount\
    = brand_id_test_feature_data_1_collect.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_1_collectCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_1_cartCount\
    = brand_id_test_feature_data_1_cart.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_1_cartCount":"count"}).iloc[:,[0,1]]

#品牌 7天
brand_id_test_feature_data_7_clickCount\
    = brand_id_test_feature_data_7_click.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_7_clickCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_7_buyCount\
    = brand_id_test_feature_data_7_buy.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_7_buyCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_7_collectCount\
    = brand_id_test_feature_data_7_collect.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_7_collectCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_7_cartCount\
    = brand_id_test_feature_data_7_cart.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_7_cartCount":"count"}).iloc[:,[0,1]]
#品牌 14天
brand_id_test_feature_data_14_clickCount\
    = brand_id_test_feature_data_14_click.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_14_clickCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_14_buyCount\
    = brand_id_test_feature_data_14_buy.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_14_buyCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_14_collectCount\
    = brand_id_test_feature_data_14_collect.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_14_collectCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_14_cartCount\
    = brand_id_test_feature_data_14_cart.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_14_cartCount":"count"}).iloc[:,[0,1]]
#品牌 28天
brand_id_test_feature_data_28_clickCount\
    = brand_id_test_feature_data_28_click.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_28_clickCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_28_buyCount\
    = brand_id_test_feature_data_28_buy.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_28_buyCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_28_collectCount\
    = brand_id_test_feature_data_28_collect.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_28_collectCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_28_cartCount\
    = brand_id_test_feature_data_28_cart.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_28_cartCount":"count"}).iloc[:,[0,1]]

#用户&品牌 1天
user_brand_test_feature_data_1_clickCount\
    = user_brand_test_feature_data_1_click.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_1_clickCount":"count"}).iloc[:,[0,1,2]]
user_brand_test_feature_data_1_buyCount\
    = user_brand_test_feature_data_1_buy.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_1_buyCount":"count"}).iloc[:,[0,1,2]]
user_brand_test_feature_data_1_collectCount\
    = user_brand_test_feature_data_1_collect.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_1_collectCount":"count"}).iloc[:,[0,1,2]]
user_brand_test_feature_data_1_cartCount\
    = user_brand_test_feature_data_1_cart.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_1_cartCount":"count"}).iloc[:,[0,1,2]]

#用户&品牌 7天
user_brand_test_feature_data_7_clickCount\
    = user_brand_test_feature_data_7_click.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_7_clickCount":"count"}).iloc[:,[0,1,2]]
user_brand_test_feature_data_7_buyCount\
    = user_brand_test_feature_data_7_buy.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_7_buyCount":"count"}).iloc[:,[0,1,2]]
user_brand_test_feature_data_7_collectCount\
    = user_brand_test_feature_data_7_collect.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_7_collectCount":"count"}).iloc[:,[0,1,2]]
user_brand_test_feature_data_7_cartCount\
    = user_brand_test_feature_data_7_cart.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_7_cartCount":"count"}).iloc[:,[0,1,2]]
#用户&品牌 14天
user_brand_test_feature_data_14_clickCount\
    = user_brand_test_feature_data_14_click.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_14_clickCount":"count"}).iloc[:,[0,1,2]]
user_brand_test_feature_data_14_buyCount\
    = user_brand_test_feature_data_14_buy.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_14_buyCount":"count"}).iloc[:,[0,1,2]]
user_brand_test_feature_data_14_collectCount\
    = user_brand_test_feature_data_14_collect.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_14_collectCount":"count"}).iloc[:,[0,1,2]]
user_brand_test_feature_data_14_cartCount\
    = user_brand_test_feature_data_14_cart.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_14_cartCount":"count"}).iloc[:,[0,1,2]]
#用户&品牌 28天
user_brand_test_feature_data_28_clickCount\
    = user_brand_test_feature_data_28_click.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_28_clickCount":"count"}).iloc[:,[0,1,2]]
user_brand_test_feature_data_28_buyCount\
    = user_brand_test_feature_data_28_buy.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_28_buyCount":"count"}).iloc[:,[0,1,2]]
user_brand_test_feature_data_28_collectCount\
    = user_brand_test_feature_data_28_collect.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_28_collectCount":"count"}).iloc[:,[0,1,2]]
user_brand_test_feature_data_28_cartCount\
    = user_brand_test_feature_data_28_cart.groupby(['user_id','brand_id'],as_index=False)['type']\
    .agg({"user_brand_test_feature_data_28_cartCount":"count"}).iloc[:,[0,1,2]]

#用户 60天
user_id_test_feature_data_60_clickCount\
    = user_id_test_feature_data_60_click.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_60_clickCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_60_buyCount\
    = user_id_test_feature_data_60_buy.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_60_buyCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_60_collectCount\
    = user_id_test_feature_data_60_collect.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_60_collectCount":"count"}).iloc[:,[0,1]]
user_id_test_feature_data_60_cartCount\
    = user_id_test_feature_data_60_cart.groupby(['user_id'],as_index=False)['type']\
    .agg({"user_id_test_feature_data_60_cartCount":"count"}).iloc[:,[0,1]]
#品牌 60天
brand_id_test_feature_data_60_clickCount\
    = brand_id_test_feature_data_60_click.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_60_clickCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_60_buyCount\
    = brand_id_test_feature_data_60_buy.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_60_buyCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_60_collectCount\
    = brand_id_test_feature_data_60_collect.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_60_collectCount":"count"}).iloc[:,[0,1]]
brand_id_test_feature_data_60_cartCount\
    = brand_id_test_feature_data_60_cart.groupby(['brand_id'],as_index=False)['type']\
    .agg({"brand_id_test_feature_data_60_cartCount":"count"}).iloc[:,[0,1]]

# 特征合并
# user_brand__dataFeature=
# 先合并用户特征（16+4+3）（23）


user_feature = user_id_test_feature_data_1_clickCount \
    .merge(user_id_test_feature_data_1_buyCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_1_collectCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_1_cartCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_7_clickCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_7_buyCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_7_collectCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_7_cartCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_14_clickCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_14_buyCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_14_collectCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_14_cartCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_28_clickCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_28_buyCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_28_collectCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_28_cartCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_60_clickCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_60_buyCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_60_collectCount, how='outer', on=['user_id']) \
    .merge(user_id_test_feature_data_60_cartCount, how='outer', on=['user_id'])

brand_feature = brand_id_test_feature_data_1_clickCount \
    .merge(brand_id_test_feature_data_1_buyCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_1_collectCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_1_cartCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_7_clickCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_7_buyCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_7_collectCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_7_cartCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_14_clickCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_14_buyCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_14_collectCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_14_cartCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_28_clickCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_28_buyCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_28_collectCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_28_cartCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_60_clickCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_60_buyCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_60_collectCount, how='outer', on=['brand_id']) \
    .merge(brand_id_test_feature_data_60_cartCount, how='outer', on=['brand_id'])

user_brand_feature = user_brand_test_feature_data_1_clickCount \
    .merge(user_brand_test_feature_data_1_buyCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_1_collectCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_1_cartCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_7_clickCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_7_buyCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_7_collectCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_7_cartCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_14_clickCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_14_buyCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_14_collectCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_14_cartCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_28_clickCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_28_buyCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_28_collectCount, how='outer', on=['user_id', 'brand_id']) \
    .merge(user_brand_test_feature_data_28_cartCount, how='outer', on=['user_id', 'brand_id'])

total = user_brand_feature \
    .merge(user_feature, how="outer", on=['user_id']) \
    .merge(brand_feature, how="outer", on=['brand_id']) \
    .merge(brand_rate_buyOfClick, how="outer", on=['brand_id']) \
    .merge(brand_rate_buyOfCollect, how="outer", on=['brand_id']) \
    .merge(brand_rate_buyOfCart, how="outer", on=['brand_id']) \
    .merge(user_rate_buyOfClick, how="outer", on=['user_id']) \
    .merge(user_rate_buyOfCollect, how="outer", on=['user_id']) \
    .merge(user_rate_buyOfCart, how="outer", on=['user_id'])

# 取2013-6-16至2013-7-15的数据贴标签
user_brand__dataLabel = test_label_data.iloc[:, [0, 1, 2]]
user_brand__dataLabel = user_brand__dataLabel[user_brand__dataLabel['type'] == 1]
user_brand__dataLabel=user_brand__dataLabel.drop_duplicates()
user_brand__dataLabel.rename(columns={'type':'tag'},inplace=True)
print user_brand__dataLabel.head(2)
#贴
testDataSet=total.merge(user_brand__dataLabel,how="outer",on=['user_id','brand_id'])
testDataSet=testDataSet.fillna(0)
testDataSet=testDataSet.drop_duplicates()
fillinf=np.isinf(testDataSet)
testDataSet[fillinf]=1
# print testDataSet.head(10)
# print testDataSet.head(1)

# sample=pd.concat([positive_df,negative_df],axis=0)

testDataSet.to_csv('D:\DAUM\\testDataSet.csv',index=False)