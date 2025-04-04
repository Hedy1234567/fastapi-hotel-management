import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true, // Indique que ce composant est autonome
  imports: [CommonModule, RouterModule], // Ajoute RouterModule pour utiliser routerLink

  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    // Any initialization logic, if required
  }

}
