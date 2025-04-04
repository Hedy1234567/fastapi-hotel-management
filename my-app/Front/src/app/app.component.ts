import { Component } from '@angular/core';
import { RouterModule } from '@angular/router'; // Import de RouterModule
import { CommonModule } from '@angular/common'; // Import de CommonModule
import { HotelListingComponent } from './hotel-listing/hotel-listing.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true,
  imports: [CommonModule, RouterModule] ,
  template: '<app-hotel-listing />',
// Ajouter ces modules dans imports
})
export class AppComponent {
  title = 'Angular App';
}
