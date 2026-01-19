package com.scysco.unitutor.eventos;

import javax.swing.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

/*
   Sin relevancia para la actividad, aqui se getiona el movimiento de la venta 
   arrastrando desde el area verde (header)
   */
public class ListenerMoverVentana extends MouseAdapter {

  private JFrame ventana;
  private int xMouse, yMouse;

  public ListenerMoverVentana(JFrame ventana) {
    this.ventana = ventana;
  }

  @Override
  public void mousePressed(MouseEvent e) {
    xMouse = e.getX();
    yMouse = e.getY();
  }

  @Override
  public void mouseDragged(MouseEvent e) {
    int xScreen = e.getXOnScreen();
    int yScreen = e.getYOnScreen();
    ventana.setLocation(xScreen - xMouse, yScreen - yMouse);
  }
}
