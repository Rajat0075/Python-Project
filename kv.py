kv_code = """
<DrawerClickableItem@MDNavigationDrawerItem>
	focus_color: "#e7e4c0"
	text_color:  "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"
    

<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True

MDScreen:
    MDNavigationLayout:
		MDScreenManager:
			MDScreen:
				MDTopAppBar:
					title: "Document"
					elevation: 4
					pos_hint: {"top":1}
					md_bg_color: "#4a4939"
					left_action_items:
						[['menu',lambda x: nav_drawer.set_state("open")]]
				ScreenManager:
				    id: sm_sub
				    Screen:
				    	name:"screen_home"
				    	MDLabel:
				    		text:"Home"
				    		pos_hint:{'center_x':1}
				    Screen:
				    	name:"screen_about"
				    	MDLabel:
				    		text:"About"
				    		pos_hint:{'center_x':1}
				    Screen:
				        name:"screen_signup"
				        MDLabel:
				        	text:"SignUp"
				        	pos_hint:{'center_x':0.5,'center_y':0.9}
				        MDTextField:
				        	icon_right: 'name'
				        	hint_text: "Name"
				        	mode: "rectangle"
				        	max_text_length: '11'
				        	pos_hint:{'center_x':0.5,'center_y':0.8}
				        MDTextField:
				        	icon_right: 'account'
				        	hint_text: "Username"
				        	mode: "rectangle"
				        	max_text_length: '11'
				        	pos_hint:{'center_x':0.5,'center_y':0.7}
				        MDTextField:
				        	icon_right:'phone'
				        	hint_text: "Phone No."
				        	mode: "rectangle"
				        	max_text_length:'10'
				            pos_hint:{'center_x':0.5,'center_y':0.6}
				        MDTextField:
				        	icon_left:'passport'
				        	hint_text: "Password"
				        	mode: "rectangle"
				        	max_text_length:'10'
				            pos_hint:{'center_x':0.5,'center_y':0.5}
				        
		MDNavigationDrawer:
			id: nav_drawer
			radius: (0,16,16,0)
			
			MDNavigationDrawerMenu:
				MDNavigationDrawerHeader:
					title: "Header Title"
					title_color: "4a4939"
					text: "Header Text"
					spacing: "4dp"
					padding: "12dp", 0,0, "56dp"
				DrawerClickableItem:
					icon: "home"
					text: "Home"
					on_release:
						sm_sub.current='screen_home'
				MDNavigationDrawerDivider:
				MDNavigationDrawerLabel:
					text:"File Operations"
				DrawerClickableItem:
					icon:"file"
					text:"New File"
				DrawerClickableItem:
					icon:"delete"
					text:"Delete"
				MDNavigationDrawerDivider:
				MDNavigationDrawerLabel:
					text: "Mail"
				DrawerClickableItem:
					icon: "gmail"
					right_text: "+99"
					text_right_color: "4a4939"
					text: "Inbox"
				DrawerClickableItem:
					icon: "send"
					text: "Outbox"
					
				MDNavigationDrawerDivider:
					
				MDNavigationDrawerLabel:
					text: "Labels"
				
				DrawerLabelItem:
					icon: "information-outline"
					text: "Label"
					
				DrawerLabelItem:
					icon: "information-outline"
					text: "Label"
					
				MDNavigationDrawerDivider:
				MDNavigationDrawerLabel:
					text: "Settings"
				DrawerClickableItem:
					icon: "information-outline"
					text: "About Us"
					on_release:
						sm_sub.current='screen_about'
				DrawerClickableItem:
					icon: "logout"
					text: "logout"
					on_release:
						sm_sub.current='screen_signup'
    MDFloatingActionButtonSpeedDial:
        data: app.data
        root_button_anim: True
		
"""
