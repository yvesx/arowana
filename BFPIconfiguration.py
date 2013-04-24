from datetime import datetime
import time
class config:
    def __init__(self,start_date="2012-10-01", end_date="2013-01-01",src='FB'):
        self.src = src
        self.start_date_unix = int(time.mktime(datetime.strptime(start_date, "%Y-%m-%d").timetuple()))
        self.end_date_unix = int(time.mktime(datetime.strptime(end_date, "%Y-%m-%d").timetuple()))
        self.max_user_per_walls  = {"FB":400000,"TW":200000} # the most recent x number of IDs to retrieve for a wall
        self.max_user_per_wall = self.max_user_per_walls[src]
        self.BF_capacities ={"FB":400000,"TW":200000}

        # template for creating future bf. so they all have same hash keys
        self.BF_default_objs ={"FB":"514cc365ba138570c53a7506","TW":"5121403fd3472f4844b8db08"}
        self.BF_capacity = self.BF_capacities[src]
        self.BF_default_obj = self.BF_default_objs[src]
        self.BF_tmp_file_path = '/tmp/'
        self.BF_tmp_file_suffixes = {"FB":"_%s_%s_sel.bloom" % (start_date , end_date),
                                    "TW":"_%s_%s_tw.bloom" % (start_date , end_date)}
        self.BF_tmp_file_suffix = self.BF_tmp_file_suffixes[src]
        self.BF_tmp_all_files = self.BF_tmp_file_path + '*' + self.BF_tmp_file_suffix        
        self.BF_tmp_entirely_all_files = self.BF_tmp_file_path + '*.bloom'               
        self.BF_false_positive = 0.01 # this combination yields a BF size just under 1MB.
        self.total_user_estimations = {"FB":200000000.0,"TW":50000000.0}
        self.total_user_estimation = self.total_user_estimations[src] # estimated pool size. use float instead of int
        ################### front/end db
        self.db_host_2 = 'xxxxx'
        self.db_port_2 = 3306
        self.db_user_2 = 'xxxxx'
        self.db_passwd_2 = 'xxxxx'
        self.db_db_2 = 'xxxxx'

        self.db_host_3 = 'xxxx'
        self.db_port_3 = 3306
        self.db_user_3 = 'xxxx'
        self.db_passwd_3 = 'xxxxx'
        self.db_db_3 = 'xxxxx'

        self.db_host_tw = 'xxxxx'
        self.db_port_tw = 3306
        self.db_user_tw = 'xxxxxx'
        self.db_passwd_tw = 'xxxxxxx'
        self.db_db_tw = 'xxxxxx'

        self.db_host_s = {"FB":self.db_host_3,"TW":self.db_host_tw}
        self.db_port_s = {"FB":self.db_port_3,"TW":self.db_port_tw}
        self.db_user_s = {"FB":self.db_user_3,"TW":self.db_user_tw}
        self.db_passwd_s = {"FB":self.db_passwd_3,"TW":self.db_passwd_tw}
        self.db_db_s = {"FB":self.db_db_3,"TW":self.db_db_tw}

        self.pl_suffix  = '_post_like_at'
        self.cmt_suffix = '_comment_at'
        self.pl_date = 'post_date'
        self.cmt_date = 'comment_date'

        ################### optimal post location
        self.db_host_post = 'xxxxxxx'
        self.db_port_post = 3306
        self.db_user_post = 'xxxxx'
        self.db_passwd_post = 'xxxx'
        self.post_db = 'xxxxx'
        self.post_old_db = 'fb_fe'
        self.post_fake_table_suffix = '_comment'
        self.post_table_suffix = '_post_id_dim'
        self.post_order_by = ['num_of_post_likes' , 'num_of_comments' , 'num_of_shares']
        self.post_popularity_strata = 10
        self.wc_db = "word_cloud"
        self.wc_prefix = "fb_"
        self.wc_suffix = "_featurestat"
        self.wc_phrase_lim = 200
        self.category_member_max = 50
        ################### backend only copy
        self.db_host_3 = 'xxxxxx'
        self.db_port_3 = 3306
        self.db_user_3 = 'xxxxx'
        self.db_passwd_3 = 'xxxxx'
        self.interest_db = 'new_precise_interest' # destination
        self.interest_table = 'new_precise_interest'
        self.category_db_table = "fb_fe.category"
        ################### frontend master copy
        self.db_host_fe = 'xxxxxx'
        self.db_port_fe = 3306
        self.db_user_fe = 'xxxxx'
        self.db_passwd_fe = 'xxxxxx'
        self.oldSchema = 'internal'
        self.oldSuffix = '_genderFm_localeall_TOTusr10_COMusr2_sort2_like2_lift'
        # works only on guru4!!
        #self.log_path_prefix = ' /files2/sphinx-data/log/pi_log_'
        #self.err_path_prefix = ' /files2/sphinx-data/log/pi_err_'
        # this is for guru web server
        self.log_path_prefix = ' xxxxx'
        self.err_path_prefix = ' xxxxxxx_'

        ################### for fbcl_access on mongo
        self.MONGO_CONNECTIONS = {
                'default': {'hosts': ["",""],
                        'port': 33333333,
                        'name': {"FB":'voxsup-fb',
                                 "TW":"voxsup-twitter",
                                 "TB":"voxsup-twitter",
                                 "INM":"voxsup-twitter",
                                 "INC":"voxsup-twitter"},
                        'username': 'xxxxxx',
                        'password': 'xxxxxxx'}
                }

        self.mongo_collection = {"FB":'bloom_filters_new',
                                 "TW":"twitter_bloomfilter"}

        self.mongo_interest_collection = {   "FB":'precise_interests',
                                             "TW":"tw_precise_interests"}
                                             
        self.mongo_general_interest_collection = {   "FB":'three_item_interests',
                                                     "TW":"three_item_interests"}

        self.mongo_index_collection = {   "FB":'category_index',
                                          "TW":""}
