using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OnMouseDown_Hide : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnMouseDown()              // 터치하면
    {
        this.gameObject.SetActive(false);   // 지운다
    }
}
