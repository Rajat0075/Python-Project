design="""
ScreenManager:
  id: sm_main
  Screen:
    name:"screen_login"
    id: screen_login
    BoxLayout:
      orientation: 'vertical'
      MDLabel:
        text: "Login Screen"
        pos_hint:{'center_x':.95}
      Button:
        text:"login button"
        on_release:
          print('screens:', sm_main.screens)
          sm_main.current='screen_app'
  Screen:
    name:"screen_app"
    id: app_screens
    BoxLayout:
      orientation: 'vertical'
      #Comment MDToolbar section to remove toolbar and still maintain full fucntionality
      MDTopAppBar:
        title: "Application Toolbar"
        size_hint: (1, 0.1)
        elevation: 10
        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
      #End MDToolbar section
      ScreenManager:
        id: sm_sub
        Screen:
          name:"screen_app_activity"
          MDLabel:
            text:"Activity Screen Label"
            pos_hint:{'center_x':1}
        Screen:
          name:"screen_app_table"
          MDLabel:
            text:"Table Screen Label"
            pos_hint:{'center_x':1}
    MDNavigationDrawer:
      id: nav_drawer
      BoxLayout:
        orientation: 'vertical'
        Button:
          text:"activity screen"
          on_release:
            sm_sub.current='screen_app_activity'
        Button:
          text:"table screen"
          on_release:
            sm_sub.current='screen_app_table'
   """
