agenda_messages = {
    "banned": {
        "keywords": ["You were banned by MTA", "Orkniowenne: MTA", "[CD47]"],
        "regex": "",
        "reply_message": "If you have been globally banned on MTA, please read our ban appeals "
                         "section: https://forum.mtasa.com/forum/180-ban-appeals/",
        "alt_message": "time_banned"
    },

    "out_of_memory": {
        "keywords": ["0x003C91CC"],
        "regex": "[oO0]x..3C91CC",
        "reply_message": "Out of video memory. This can happen on servers with unoptimized mods "
                         "and (faulty) scripts that abuse video memory, or even when you have a "
                         "powerful graphics card in case the stuff on a server is extremely "
                         "unoptimized so that it starts hitting GTA limits. If you have a powerful "
                         "graphics card and more players suffer from this crash type, inform the "
                         "server owner of this problem as it probably means their scripters & "
                         "designers don't know what they are doing.",
        "alt_message": ""
    },

    "time_banned": {
        "keywords": ["Time Remaining"],
        "regex": "",
        "reply_message": "You have been banned from MTA temporarily, you cannot appeal for a timed ban, please wait "
                         "for you ban to expire ",
        "alt_message": ""
    }
}


def get_messages_agenda_dict():
    return agenda_messages
