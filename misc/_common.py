from arcgis.gis import GIS

"""accounts to keep from user/groups/items deletion"""
ignore_accounts_online = ['DavidJVitale', 'yjiang_geosaurus', 'amani_geosaurus', 'api_data_owner',
                   'bmajor_geosaurus', 'rsingh_geosaurus', 'rohitgeo', 'andrew887',
                   'cwhitmore_geosaurus', 'ArcGISPyAPIBot', 'jyaist_geosaurus', 'cpeng_geosaurus', 'MMajumdar_geosaurus']

ignore_accounts_playground = ['andrew', 'andrew.chapkowski', 'apulver', 'dvitale', 'david.vitale',
                   'atma.mani', 'john.yaist', 'bill.major', 'YJiang',
                   'rohit.singh', 'rohitgeo', 'gbochenek_python',
                   'system_publisher', 'admin', 'portaladmin',
                   'Demo_User', 'First_User', 'Second_User',
                   'api_data_owner', 'arcgis_python', 'temp_execution']

"""accounts that you want to delete groups and items, but keep user"""
target_accounts_online = ['arcgis_python']
target_accounts_playground = ['arcgis_python']

"""data to publish"""
data_paths = [r'\\archive\crdata\Geosaurus_datasets\data_prep\csv\Trailheads.csv']

"""create GIS connection via admin credentials"""
gis_online = GIS(profile="your_online_admin_profile")
gis_playground = GIS(profile='your_ent_admin_profile')


def delete_depending_items(dependent_item):
    """deletes the item's depending items, and then the item"""
    depending_items = None
    try:
        depending_items = dependent_item.dependent_to()
        if depending_items['list']:
            for item in depending_items['list']:
                delete_depending_items(item)
    except:
        print("=== could not get item list %s" % dependent_item.homepage)

    if dependent_item.protected:
        dependent_item.protect(False)
    try:
        print("=== deleting the item: %s" % dependent_item.homepage)
        dependent_item.delete()
    except:
        print("=== could not delete non-dependent item %s" % dependent_item.homepage)


def delete_items(user):
    """deletes the user items"""
    folders = [None] + user.folders
    for folder in folders:
        print("=== deleting inside folder: %s" % folder)
        for item in user.items(folder=folder, max_items=255):
            delete_depending_items(item)
    print("=== finished deleting items owned by " + user.username)


def delete_groups(gis, user):
    """deletes the user groups, and removes user from groups where user is a member of"""
    groups_for_deletion = gis.groups.get('query=owner:' + user.username)
    if groups_for_deletion is not None:
        for group in groups_for_deletion:
            try:
                print("=== deleting group %s" % group.groupid)
                group.delete()
            except:
                print("=== could not delete group %s" % group.groupid)

    for grp in user.groups:
        print("=== removing from group: %s" % grp.id)
        if grp.owner != user.username:
            try:
                grp.remove_users([user.username])
            except:
                print("=== User cannot be removed from group: %s" % grp.id)
    print("=== finished deleting groups owned by " + user.username)


def delete_for_users(gis, ignore_accounts, target_accounts):
    """deletes items and groups for users in target_accounts, and ignore others"""
    for user in gis.users.search():
        if user.username not in ignore_accounts and not user.username.startswith("esri_"):
            print("-*-*-*-*-*-*-Delete groups & items & user for %s -*-*-*-*-*-" % user.username)
            delete_items(user)
            delete_groups(gis, user)
            try:
                user.delete()
            except:
                print("could not delete user %s" % user.username)
        elif user.username in target_accounts:
            print("-*-*-*-*-*-*-Delete groups & items for %s -*-*-*-*-*-*-*-*-" % user.username)
            delete_items(user)
            delete_groups(gis, user)

        else:
            print("-*-*-*-*-*-*-*-*-No Delete for %s -*-*-*-*-*-*-*-*-*-*-" % user.username)


def publish_data(gis, paths):
    """publish sample data"""
    for path in paths:
        item = gis.content.add({}, path)
        item.share(everyone=True)
        lyr = item.publish()


def clean_up_location_tracking(gis):
    # disable location tracking
    if gis.admin.location_tracking.status != "disabled":
        gis.admin.location_tracking.disable()

    roles = gis.users.roles.all()
    for role in roles:
        if role.name == "Track Viewer":
            role.delete()
            break


def setup_tracker_user(gis):
    # create the track_viewer account
    tracker_demo = gis.users.get('tracker_demo')
    if tracker_demo is None:
        tracker_demo = gis.users.create(username='tracker_demo',
                         password='b0cb0c9f63e',
                         firstname='Tracker',
                         lastname='Demo',
                         email='python@esri.com',
                         description='demo track viewer account',
                         role='org_user')
    else:
        tracker_demo.update_role('org_user')
