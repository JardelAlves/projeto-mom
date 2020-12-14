import pygame
import pygame_gui

from client_interface import Client
from client_interface import DaemonThread

from threading import Thread
from pygame_gui.elements.ui_selection_list import UISelectionList


green = (0, 255, 0)
blue = (0, 0, 100)
white = (255, 255, 255)
grey = (235, 235, 235)

chat = Client()
daemonThread = DaemonThread(chat)
daemonThread.start()
chat.start_conexao()
chat.createChatHistory()
agenda = chat.getAgenda()
agenda.remove(chat.nick)
pygame.init()
html = """"""
html = html + chat.chat_history
screen = pygame.display.set_mode([600, 500])
manager = pygame_gui.UIManager((600, 500), "style.JSON")
nickname = chat.nick
pygame.display.set_caption(f'Chat - {nickname}')

recieve = len(chat.chat_history)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(f'{nickname}', True, blue, grey)
textRect = text.get_rect()
textRect.center = (300, 30)

button_offline = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(485, 100, 90, 30),
                                            text='Offline',
                                            manager=manager)

chat_textBox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(10, 60, 350, 400),
                                            html_text=html,
                                            manager=manager)


chat_entryText = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(10, 460, 350, 200),
                                            manager=manager)

button_online = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(385, 100, 90, 30),
                                            text='Online',
                                            manager=manager)


lista = UISelectionList(relative_rect=pygame.Rect(405, 200, 150, 146),
                                            item_list=agenda,
                                            manager=manager)

screen.fill(grey)
clock = pygame.time.Clock()


manager.draw_ui(screen)
pygame.display.flip()

chat_context = None

running = True
while running:
    time_delta = clock.tick(60) / 1000.0

    screen.blit(text, textRect)

    if recieve < len(chat.chat_history) and chat_context != None:
        chat_textBox.kill()
        html = chat.chat_history
        chat_textBox = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(10, 60, 350, 400),
                                            html_text=html,
                                            manager=manager)
        recieve = len(chat.chat_history)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                texto = chat_entryText.get_text()
                chat.chat_history = chat.chat_history + str('<font  color=#0000FF>' + nickname + ":" + " " + str(texto) + '<br>' + '</font>')
                chat_entryText.set_text('')
                if t:
                    n = [d for d, e in enumerate(chat.client_context) if e["name"] == t]
                    m = n[0]
                    chat.client_context[m]["chatHistory"] = chat.chat_history
                    chat.send(texto,t)
        if event.type == pygame.USEREVENT:
            if event.user_type == 'ui_button_pressed':
                if event.ui_element == button_offline:
                    chat.setOffline()
                    chat.chat_history = chat.chat_history + str('<font  color=#0000FF>' + 'Você está offline' + '<br>' + '</font>')
                elif event.ui_element == button_online:
                    chat.setOnline()
                    chat.chat_history = chat.chat_history + str('<font  color=#0000FF>' + 'Você está online' + '<br>' + '</font>')

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                if event.ui_element == lista:
                    t = lista.get_single_selection()
                    n = [d for d, e in enumerate(chat.client_context) if e["name"] == t]
                    m = n[0]
                    chat_context = chat.client_context[m]["name"]
                    chat.contexto = chat_context
                    chat.chat_history = chat.client_context[m]["chatHistory"]
                    recieve = len(chat.client_context[m]["chatHistory"])
                    if recieve == 0:
                        chat.chat_history = chat.chat_history + str('<font  color=#0000FF>' + 'Chat iniciado com ' + t + '<br>' + '</font>')
                    else:
                        print(chat.chat_history)
                        recieve = 0

        manager.process_events(event)

    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.flip()
    pygame.event.pump()