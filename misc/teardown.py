from _common import *

print("-*-*-*-*-*-*-*-*-*-*-*Teardown begins*-*-*-*-*-*-*-*-*-*-*-*-")

clean_up_location_tracking(gis_playground)
delete_for_users(gis_online, ignore_accounts_online, target_accounts_online)
delete_for_users(gis_playground, ignore_accounts_playground, target_accounts_playground)
# publish_data(gis_online, data_paths)

print("-*-*-*-*-*-*-*-*-*-*-*Teardown ends*-*-*-*-*-*-*-*-*-*-*-*-*-")
