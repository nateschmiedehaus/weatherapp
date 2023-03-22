def update_facebook_ad_spend(ad_spend_data, facebook_access_token):
    # Replace with the actual endpoint, parameters, and access token
    url = f'https://graph.facebook.com/v13.0/{ad_spend_data["ad_id"]}?access_token={facebook_access_token}'
    payload = {
        'daily_budget': ad_spend_data['new_daily_budget']
    }
    response = requests.post(url, data=payload)
    result = response.json()
    return result

    