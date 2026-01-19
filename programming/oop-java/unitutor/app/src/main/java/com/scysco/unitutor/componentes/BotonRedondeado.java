package com.scysco.unitutor.componentes;

import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;

/*
   Simplemente un componente reutilizable que separo de la otra lógica para que sea mas fácil de leer
   */
public class BotonRedondeado extends JButton {

  private int radius;
  private Color borderColor;

  public BotonRedondeado(String texto, int radius, Color borderColor) {
    super(texto);
    this.radius = radius;
    this.borderColor = borderColor;
    setContentAreaFilled(false);
    setFocusPainted(false);
    setBorder(new EmptyBorder(0, 20, 0, 20));
  }

  public void setBorderColor(Color newColor) {
    this.borderColor = newColor;
    repaint();
  }

  @Override
  protected void paintComponent(Graphics g) {
    Graphics2D g2 = (Graphics2D) g.create();
    g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
    g2.setColor(getBackground());
    g2.fillRoundRect(0, 0, getWidth() - 1, getHeight() - 1, radius, radius);
    g2.setColor(borderColor);
    g2.drawRoundRect(0, 0, getWidth() - 1, getHeight() - 1, radius, radius);
    g2.dispose();
    super.paintComponent(g);
  }
}
