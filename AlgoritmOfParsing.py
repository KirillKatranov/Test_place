def parsing_posts(amount_posts):
    amount_group = 30
    if amount_posts >= amount_group:
        amount_posts_from_single_group = amount_posts // amount_group
        amount_group_add_1post = amount_posts - (amount_group * amount_posts_from_single_group)
        for group in range(amount_group):
            if group < amount_group_add_1post:
                amount_posts_from_single_group += 1
            for post in range(amount_posts_from_single_group):
                pass
            amount_posts_from_single_group -= 1
    else:
        for group in range(amount_group):
            

if __name__ == "__main__":
    parsing_posts(100)