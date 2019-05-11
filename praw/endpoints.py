"""List of API endpoints PRAW knows about."""

# flake8: noqa
# fmt: off
API_PATH = {
    "about_edited":            "r/{subreddit}/about/edited/",
    "about_log":               "r/{subreddit}/about/log/",
    "about_modqueue":          "r/{subreddit}/about/modqueue/",
    "about_reports":           "r/{subreddit}/about/reports/",
    "about_spam":              "r/{subreddit}/about/spam/",
    "about_sticky":            "r/{subreddit}/about/sticky/",
    "about_stylesheet":        "r/{subreddit}/about/stylesheet/",
    "about_traffic":           "r/{subreddit}/about/traffic/",
    "about_unmoderated":       "r/{subreddit}/about/unmoderated/",
    "accept_mod_invite":       "r/{subreddit}/api/accept_moderator_invite",
    "approve":                 "api/approve/",
    "block":                   "api/block",
    "block_user":              "/api/block_user/",
    "blocked":                 "prefs/blocked/",
    "collapse":                "api/collapse_message/",
    "collection":              "api/v1/collections/collection",
    "collection_add_post":     "api/v1/collections/add_post_to_collection",
    "collection_create":       "api/v1/collections/create_collection",
    "collection_delete":       "api/v1/collections/delete_collection",
    "collection_desc":         "api/v1/collections/update_collection_description",
    "collection_follow":       "api/v1/collections/follow_collection",
    "collection_remove_post":  "api/v1/collections/remove_post_in_collection",
    "collection_reorder":      "api/v1/collections/reorder_collection",
    "collection_subreddit":    "api/v1/collections/subreddit_collections",
    "collection_title":        "api/v1/collections/update_collection_title",
    "comment":                 "api/comment/",
    "comment_replies":         "message/comments/",
    "compose":                 "api/compose/",
    "contest_mode":            "api/set_contest_mode/",
    "del":                     "api/del/",
    "delete_message":          "api/del_msg",
    "delete_sr_banner":        "r/{subreddit}/api/delete_sr_banner",
    "delete_sr_header":        "r/{subreddit}/api/delete_sr_header",
    "delete_sr_icon":          "r/{subreddit}/api/delete_sr_icon",
    "delete_sr_image":         "r/{subreddit}/api/delete_sr_img",
    "deleteflair":             "r/{subreddit}/api/deleteflair",
    "distinguish":             "api/distinguish/",
    "domain":                  "domain/{domain}/",
    "duplicates":              "duplicates/{submission_id}/",
    "edit":                    "api/editusertext/",
    "emoji_delete":            "api/v1/{subreddit}/emoji/{emoji_name}",
    "emoji_lease":             "api/v1/{subreddit}/emoji_asset_upload_s3.json",
    "emoji_list":              "api/v1/{subreddit}/emojis/all",
    "emoji_upload":            "api/v1/{subreddit}/emoji.json",
    "flair":                   "r/{subreddit}/api/flair/",
    "flairconfig":             "r/{subreddit}/api/flairconfig/",
    "flaircsv":                "r/{subreddit}/api/flaircsv/",
    "flairlist":               "r/{subreddit}/api/flairlist/",
    "flairselector":           "r/{subreddit}/api/flairselector/",
    "flairtemplate":           "r/{subreddit}/api/flairtemplate/",
    "flairtemplate_v2":        "r/{subreddit}/api/flairtemplate_v2",
    "flairtemplateclear":      "r/{subreddit}/api/clearflairtemplates/",
    "flairtemplatedelete":     "r/{subreddit}/api/deleteflairtemplate/",
    "friend":                  "r/{subreddit}/api/friend/",
    "friend_v1":               "api/v1/me/friends/{user}",
    "friends":                 "api/v1/me/friends/",
    "gild_thing":              "api/v1/gold/gild/{fullname}/",
    "gild_user":               "api/v1/gold/give/{username}/",
    "hide":                    "api/hide/",
    "ignore_reports":          "api/ignore_reports/",
    "inbox":                   "message/inbox/",
    "info":                    "api/info/",
    "karma":                   "api/v1/me/karma",
    "leavecontributor":        "api/leavecontributor",
    "link_flair":              "r/{subreddit}/api/link_flair_v2",
    "list_banned":             "r/{subreddit}/about/banned/",
    "list_contributor":        "r/{subreddit}/about/contributors/",
    "list_moderator":          "r/{subreddit}/about/moderators/",
    "list_muted":              "r/{subreddit}/about/muted/",
    "list_wikibanned":         "r/{subreddit}/about/wikibanned/",
    "list_wikicontributor":    "r/{subreddit}/about/wikicontributors/",
    "live_accept_invite":      "api/live/{id}/accept_contributor_invite",
    "live_add_update":         "api/live/{id}/update",
    "live_close":              "api/live/{id}/close_thread",
    "live_contributors":       "live/{id}/contributors",
    "live_discussions":        "live/{id}/discussions",
    "live_focus":              "live/{thread_id}/updates/{update_id}",
    "live_info":               "api/live/by_id/{ids}",
    "live_invite":             "api/live/{id}/invite_contributor",
    "live_leave":              "api/live/{id}/leave_contributor",
    "live_now":                "api/live/happening_now",
    "live_remove_contrib":     "api/live/{id}/rm_contributor",
    "live_remove_invite":      "api/live/{id}/rm_contributor_invite",
    "live_remove_update":      "api/live/{id}/delete_update",
    "live_report":             "api/live/{id}/report",
    "live_strike":             "api/live/{id}/strike_update",
    "live_update_perms":       "api/live/{id}/set_contributor_permissions",
    "live_update_thread":      "api/live/{id}/edit",
    "live_updates":            "live/{id}",
    "liveabout":               "api/live/{id}/about/",
    "livecreate":              "api/live/create",
    "lock":                    "api/lock/",
    "marknsfw":                "api/marknsfw/",
    "me":                      "api/v1/me",
    "media_asset":             "api/media/asset.json",
    "mentions":                "message/mentions",
    "message":                 "message/messages/{id}/",
    "messages":                "message/messages/",
    "moderator_messages":      "r/{subreddit}/message/moderator/",
    "moderator_unread":        "r/{subreddit}/message/moderator/unread/",
    "modmail_archive":         "api/mod/conversations/{id}/archive",
    "modmail_bulk_read":       "api/mod/conversations/bulk/read",
    "modmail_conversation":    "api/mod/conversations/{id}",
    "modmail_conversations":   "api/mod/conversations/",
    "modmail_highlight":       "api/mod/conversations/{id}/highlight",
    "modmail_mute":            "api/mod/conversations/{id}/mute",
    "modmail_read":            "api/mod/conversations/read",
    "modmail_subreddits":      "api/mod/conversations/subreddits",
    "modmail_unarchive":       "api/mod/conversations/{id}/unarchive",
    "modmail_unmute":          "api/mod/conversations/{id}/unmute",
    "modmail_unread":          "api/mod/conversations/unread",
    "modmail_unread_count":    "api/mod/conversations/unread/count",
    "morechildren":            "api/morechildren/",
    "multireddit":             "user/{user}/m/{multi}/",
    "multireddit_api":         "api/multi/user/{user}/m/{multi}/",
    "multireddit_base":        "api/multi/",
    "multireddit_copy":        "api/multi/copy/",
    "multireddit_rename":      "api/multi/rename/",
    "multireddit_update":      "api/multi/user/{user}/m/{multi}/r/{subreddit}",
    "multireddit_user":        "api/multi/user/{user}/",
    "mute_sender":             "api/mute_message_author/",
    "my_contributor":          "subreddits/mine/contributor/",
    "my_moderator":            "subreddits/mine/moderator/",
    "my_multireddits":         "api/multi/mine/",
    "my_subreddits":           "subreddits/mine/subscriber/",
    "preferences":             "api/v1/me/prefs",
    "quarantine_opt_in":       "api/quarantine_optin",
    "quarantine_opt_out":      "api/quarantine_optout",
    "read_message":            "api/read_message/",
    "removal_comment_message": "api/v1/modactions/removal_comment_message",
    "removal_link_message":    "api/v1/modactions/removal_link_message",
    "remove":                  "api/remove/",
    "report":                  "api/report/",
    "rules":                   "r/{subreddit}/about/rules",
    "save":                    "api/save/",
    "search":                  "r/{subreddit}/search/",
    "select_flair":            "r/{subreddit}/api/selectflair/",
    "sendreplies":             "api/sendreplies",
    "sent":                    "message/sent/",
    "setpermissions":          "r/{subreddit}/api/setpermissions/",
    "site_admin":              "api/site_admin/",
    "spoiler":                 "api/spoiler/",
    "sticky_submission":       "api/set_subreddit_sticky/",
    "store_visits":            "api/store_visits",
    "structured_styles":       "api/v1/structured_styles/{subreddit}",
    "style_asset_lease":       "api/v1/style_asset_upload_s3/{subreddit}",
    "sub_recommended":         "api/recommend/sr/{subreddits}",
    "submission":              "comments/{id}/",
    "submission_replies":      "message/selfreply/",
    "submit":                  "api/submit/",
    "subreddit":               "r/{subreddit}/",
    "subreddit_about":         "r/{subreddit}/about/",
    "subreddit_filter":        "api/filter/user/{user}/f/{special}/r/{subreddit}",
    "subreddit_filter_list":   "api/filter/user/{user}/f/{special}",
    "subreddit_random":        "r/{subreddit}/random/",
    "subreddit_settings":      "r/{subreddit}/about/edit/",
    "subreddit_stylesheet":    "r/{subreddit}/api/subreddit_stylesheet/",
    "subreddits_by_topic":     "api/subreddits_by_topic",
    "subreddits_default":      "subreddits/default/",
    "subreddits_gold":         "subreddits/gold/",
    "subreddits_name_search":  "api/search_reddit_names/",
    "subreddits_new":          "subreddits/new/",
    "subreddits_popular":      "subreddits/popular/",
    "subreddits_search":       "subreddits/search/",
    "subscribe":               "api/subscribe/",
    "suggested_sort":          "api/set_suggested_sort/",
    "trophies":                "api/v1/user/{user}/trophies",
    "uncollapse":              "api/uncollapse_message/",
    "unfriend":                "r/{subreddit}/api/unfriend/",
    "unhide":                  "api/unhide/",
    "unignore_reports":        "api/unignore_reports/",
    "unlock":                  "api/unlock/",
    "unmarknsfw":              "api/unmarknsfw/",
    "unmute_sender":           "api/unmute_message_author/",
    "unread":                  "message/unread/",
    "unread_message":          "api/unread_message/",
    "unsave":                  "api/unsave/",
    "unspoiler":               "api/unspoiler/",
    "upload_image":            "r/{subreddit}/api/upload_sr_img",
    "user":                    "user/{user}/",
    "user_about":              "user/{user}/about/",
    "user_flair":              "r/{subreddit}/api/user_flair_v2",
    "users_new":               "users/new",
    "users_popular":           "users/popular",
    "users_search":            "users/search",
    "vote":                    "api/vote/",
    "widget_create":           "r/{subreddit}/api/widget",
    "widget_lease":            "r/{subreddit}/api/widget_image_upload_s3",
    "widget_modify":           "r/{subreddit}/api/widget/{widget_id}",
    "widget_order":            "r/{subreddit}/api/widget_order/{section}",
    "widgets":                 "r/{subreddit}/api/widgets",
    "wiki_edit":               "r/{subreddit}/api/wiki/edit/",
    "wiki_page":               "r/{subreddit}/wiki/{page}",
    "wiki_page_editor":        "r/{subreddit}/api/wiki/alloweditor/{method}",
    "wiki_page_revisions":     "r/{subreddit}/wiki/revisions/{page}",
    "wiki_page_settings":      "r/{subreddit}/wiki/settings/{page}",
    "wiki_pages":              "r/{subreddit}/wiki/pages/",
    "wiki_revisions":          "r/{subreddit}/wiki/revisions/",
}
