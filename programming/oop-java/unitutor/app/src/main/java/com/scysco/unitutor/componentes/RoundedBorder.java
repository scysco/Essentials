package com.scysco.unitutor.componentes;

import javax.swing.border.AbstractBorder;
import java.awt.*;
import java.awt.geom.RoundRectangle2D;

/*
   Un border personalizado que separo de la lógica para tener un código mas limpio
   */
public class RoundedBorder extends AbstractBorder {

  private int radius;
  private Color color;

  public RoundedBorder(int radius, Color color) {
    this.radius = radius;
    this.color = color;
  }

  @Override
  public void paintBorder(Component c, Graphics g, int x, int y, int width, int height) {
    Graphics2D g2d = (Graphics2D) g.create();
    g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
    g2d.setColor(this.color);
    g2d.draw(new RoundRectangle2D.Double(x, y, width - 1, height - 1, radius, radius));
    g2d.dispose();
  }
}
