from aiogram.types import ChatPermissions
import os
from dotenv import load_dotenv

load_dotenv(".env")

BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_OWNER = os.getenv('BOT_OWNER')
ADMINS = os.getenv('ADMINS')
GENERAL_GROUP = os.getenv('GENERAL_GROUP')
ADMIN_GROUP = os.getenv('ADMIN_GROUP')
ALL_CMD = os.getenv('ALL_CMD')


# PERMISSIONS
# MUTE AND UNMUT
permissions = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_other_messages=False,
    can_add_web_page_previews=False
)

permissions1 = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_other_messages=True,
    can_add_web_page_previews=True
)

# ADMIN AND USER
ADMIN = {'can_change_info': True, 'can_post_messages': True, 'can_edit_messages': True, 'can_delete_messages': True,
         'can_invite_users': True, 'can_restrict_members': True, 'can_pin_messages': True, 'can_promote_members': True}
ADMIN_OWNER = {'is_anonymous': True, 'can_manage_chat': True, 'can_change_info': True, 'can_post_messages': True,
               'can_edit_messages': True, 'can_delete_messages': True, 'can_manage_video_chats': True,
               'can_invite_users': True, 'can_restrict_members': True, 'can_pin_messages': True,
               'can_manage_video_chats': True, 'can_manage_topics': True}
USER = {'is_anonymous': False, 'can_manage_chat': False, 'can_change_info': False, 'can_post_messages': False,
        'can_edit_messages': False, 'can_delete_messages': False, 'can_manage_video_chats': False,
        'can_invite_users': True, 'can_restrict_members': False, 'can_pin_messages': False,
        'can_manage_video_chats': False, 'can_manage_topics': False}
