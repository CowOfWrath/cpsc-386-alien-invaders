# Ryan Chen
# 893219394
# Implementation of various game functions used in checking and updating the state of the game

import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien

def create_alien(settings, screen, aliens, alien_num, row):
    alien = Alien(settings, screen, settings.alien_width, settings.alien_height)
    alien.rect.x = settings.alien_width + 2 * settings.alien_width * alien_num
    alien.rect.y = settings.alien_height + 2 * settings.alien_height * row
  #still not sure if i want to use this  alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(settings, screen, aliens):
    space_x = settings.screen_width - 2 * (settings.alien_width)
    num_aliens_x = int(space_x / (2 * (settings.alien_width)))

    space_y = settings.screen_height - 3 * settings.alien_height - settings.ship_height
    num_rows = int(space_y / (2 * settings.alien_height))

    for row in range(num_rows):
        for alien_num in range(num_aliens_x):
            create_alien(settings, screen, aliens, alien_num, row)


def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullet_max:
        b = Bullet(settings, screen, ship)
        bullets.add(b)

def check_keydown(settings, stats, event, screen, ship, bullets):
    if event.key == pygame.K_ESCAPE:
        stats.running = False

    # Ship movement events
    elif event.key == pygame.K_RIGHT:
        settings.ship_move_right = True
        settings.ship_move_left = False
    elif event.key == pygame.K_LEFT:
        settings.ship_move_left = True
        settings.ship_move_right = False
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)


def check_keyup(settings, event):
    if event.key == pygame.K_RIGHT:
        settings.ship_move_right = False
    elif event.key == pygame.K_LEFT:
        settings.ship_move_left = False

def check_play_button(settings, screen, stats, sb, play_button, mouse_x, mouse_y,ship, aliens, bullets):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.active:
        pygame.mouse.set_visible(False)
        settings.init_dynamic_settings()
        stats.reset_stats()
        stats.active = True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()
        create_fleet(settings,screen,aliens)
        ship.center_ship()

def check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets):
    # Check key and mouse events
    for event in pygame.event.get():
        # Quit game events
        if event.type == pygame.QUIT:
            stats.running = False
        elif event.type == pygame.KEYDOWN:
            check_keydown(settings, stats, event, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(settings, event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, sb, play_button, mouse_x, mouse_y, ship, aliens, bullets)


def change_fleet_direction(settings, aliens):
    for a in aliens.sprites():
        a.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1
    aliens.update()

def check_fleet_edges(settings, aliens):
    for a in aliens.sprites():
        if a.check_edges():
            change_fleet_direction(settings, aliens)

def check_bullet_alien_collisions(settings, screen, stats, sb, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for a in collisions.values():
            stats.score += settings.alien_points
        sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens) == 0:
        settings.speedup()
        stats.level += 1
        sb.prep_level()
        bullets.empty()
        create_fleet(settings, screen, aliens)

def ship_hit(settings, screen, stats, sb, ship, aliens, bullets):
        if stats.ship_lives > 0:
            stats.ship_lives -= 1
            sb.prep_ships()
            aliens.empty()
            bullets.empty()
            ship.center_ship()
            create_fleet(settings, screen, aliens)
        else:
            stats.active = False
            pygame.mouse.set_visible(True)

def check_aliens_bottom(settings, screen, stats, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for a in aliens.sprites():
        if a.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, screen, stats, sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def update_aliens(settings, screen, stats, sb, ship, aliens, bullets):
    check_fleet_edges(settings, aliens)
    aliens.update()
    check_aliens_bottom(settings, screen, stats, sb, ship, aliens, bullets)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, screen, stats, sb, ship, aliens, bullets)

def update_bullets(settings, screen, stats, sb, aliens, bullets):
    bullets.update()

    # Manage objects
    for b in bullets:
        if b.rect.bottom <= 0:
            bullets.remove(b)
    check_bullet_alien_collisions(settings, screen, stats, sb, aliens, bullets)

def update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # update images on screen and display screen
    screen.fill(settings.bg_color)
    ship.draw()
    aliens.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw()

    sb.draw()

    if not stats.active:
        play_button.draw()

    # Update Screen
    pygame.display.flip()