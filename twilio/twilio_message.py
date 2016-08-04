from twilio.rest import TwilioRestClient

account_sid = 'AC854ad0b864882fc16e79e20c8d6f370d'
auth_token = 'ac35ad6e0417355952c3c65ff8a3f2d1'

client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(to = "+5215524968413", from_="+12018066572",
                                body = "Jojojojo jejejeje jujuj")
