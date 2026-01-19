package com.scysco.unitutor.eventos;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

/*
   Sin relevancia para la actividad, aquí se gestiona el comportamiento de (X)
   */
public class ListenerCerrar extends MouseAdapter {

  private JLabel boton;

  public ListenerCerrar(JLabel boton) {
    this.boton = boton;
  }

  @Override
  public void mouseClicked(MouseEvent e) {
    System.exit(0);
  }

  @Override
  public void mouseEntered(MouseEvent e) {
    boton.setForeground(Color.RED);
  }

  @Override
  public void mouseExited(MouseEvent e) {
    boton.setForeground(Color.WHITE);
  }
}
