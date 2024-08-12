import *
# Inicialização do pygame pygame.init
()# Definição das dimensões da janela
largura = 800 altura = 600
tela = pygame.display.set_mode((largura,
altura))
pygame.display.set_caption
("Jogo de Ação")
# Definição das cores
PRETO = (0, 0, 0)BRANCO = (255, 255, 255)
# Definição das variáveis do jogador x_jogador = 50
y_jogador = 50
largura_jogador = 50
altura_jogador = 50
velocidade_jogador = 5
# Função para desenhar o jogador
na tela
def desenhar_jogador(x, y):
 pygame.draw.rect(tela, BRANCO, (x, y, largura_jogador, altura_jogador))#
 Loop principal do jogo jogo_rodando = True
while jogo_rodando: # Preenchimento da tela com a cor preta
 tela.fill(PRETO)
 # Eventos do jogo
 for evento in pygame.event.get():
 if evento.type == QUIT:
 jogo_rodando = Falso
 # Movimentação do jogador
 teclas_pressionadas = pygame.key.get_pressed()
 se teclas_pressionadas[K_UP]: y_jogador -= velocidade_jogador se teclas_pressionadas[K_DOWN]: y_jogador += velocidade_jogador se teclas_pressionadas[K_LEFT]: x_jogador -= velocidade_jogador
 se teclas_pressionadas[K_RIGHT]:
 x_jogador += velocidade_jogador
 # Desenho do jogador
 desenhar_jogador(x_jogador, y_jogador) # Atualização da tela pygame.display.update()# Encerramento do pygame pygame.quit()
''Este