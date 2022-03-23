from herald_bot.herald import Herald 



with Herald(teardown=False) as bot :
    bot.landing_page()
    bot.select_top_stories()
    bot.get_contents()
