<template>
  <v-row class="pa-6">
    <v-col cols="4">
      <v-list density="compact" rounded="lg" bg-color="#2b2a3e" class="text-medium-emphasis">
        <v-list-subheader class="text-disabled">ABOUT</v-list-subheader>
        <v-list-item class="align-center">
          <v-icon icon="mdi-account-outline"></v-icon>
          <span class="ml-2">Full Name: John Doe</span>
        </v-list-item>
        <v-list-item>
          <v-icon icon="mdi-check-bold"></v-icon>
          <span class="ml-2">Status: active</span>

        </v-list-item>
        <v-list-item title="Role: Developer"></v-list-item>
        <v-list-item title="Country: USA"></v-list-item>
        <v-list-subheader class="text-disabled">CONTACTS</v-list-subheader>
        <v-list-item title="Contact: (123) 456-7890"></v-list-item>
        <v-list-item title="Skype: john.doe"></v-list-item>
        <v-list-item title="Email: john.doe@example.com"></v-list-item>
        <v-list-subheader class="text-disabled">TEAMS</v-list-subheader>
        <v-list-item title="Backend Developer(126 Members)"></v-list-item>
        <v-list-item title="VueJS Developer(98 Members)"></v-list-item>
        <v-list-item title="Role: Developer"></v-list-item>
      </v-list>
    </v-col>

  </v-row>
</template>
<script setup lang="ts">
</script>
