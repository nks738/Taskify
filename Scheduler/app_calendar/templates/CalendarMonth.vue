<template><!-- Parent container for the calendar month -->
<div class="calendar-month"> <!-- The calendar header -->
  <div class="calendar-month-header"> <!-- Month name -->
    <CalendarDateIndicator /> <!-- Pagination -->
    <CalendarDateSelector />
  </div> <!-- Calendar grid header -->
  <CalendarWeekdays /> <!-- Calendar grid -->
  <ol class="days-grid">
    <CalendarMonthDayItem />
  </ol>
</div></template>