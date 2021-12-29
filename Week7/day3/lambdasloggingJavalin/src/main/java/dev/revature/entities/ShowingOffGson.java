package dev.revature.entities;

import java.util.Objects;

public class ShowingOffGson {
    private String stringValue;
    private int numberValue;
    private boolean booleanValue;

    // created this entity to show how to recieve and send JSONs using Gson
    public ShowingOffGson(){}

    public ShowingOffGson(String stringValue, int numberValue, boolean booleanValue) {
        this.stringValue = stringValue;
        this.numberValue = numberValue;
        this.booleanValue = booleanValue;
    }

    public String getStringValue() {
        return stringValue;
    }

    public void setStringValue(String stringValue) {
        this.stringValue = stringValue;
    }

    public int getNumberValue() {
        return numberValue;
    }

    public void setNumberValue(int numberValue) {
        this.numberValue = numberValue;
    }

    public boolean isBooleanValue() {
        return booleanValue;
    }

    public void setBooleanValue(boolean booleanValue) {
        this.booleanValue = booleanValue;
    }

    @Override
    public String toString() {
        return "ShowingOffGson{" +
                "stringValue='" + stringValue + '\'' +
                ", numberValue=" + numberValue +
                ", booleanValue=" + booleanValue +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        ShowingOffGson that = (ShowingOffGson) o;
        return numberValue == that.numberValue && booleanValue == that.booleanValue && Objects.equals(stringValue, that.stringValue);
    }

    @Override
    public int hashCode() {
        return Objects.hash(stringValue, numberValue, booleanValue);
    }
}
