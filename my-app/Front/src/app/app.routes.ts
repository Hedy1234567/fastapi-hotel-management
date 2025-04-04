import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { HotelListingComponent } from './hotel-listing/hotel-listing.component';


export const routes: Routes = [
  { path: 'login', component: LoginComponent }, // Route pour la connexion
  { path: 'hotels', component: HotelListingComponent },  // Route pour la liste des hôtels
  { path: '', component: HomeComponent } // Page d'accueil


  
];
