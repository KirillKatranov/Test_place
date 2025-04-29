import vk_api

vk_session = vk_api.VkApi(token="e597be55e597be55e597be55b0e6bc4d0aee597e597be55825e456260395ae79c4309ef")
vk_session.auth()

vk = vk_session.get_api()

print(vk.wall.post(message='Hello world!'))